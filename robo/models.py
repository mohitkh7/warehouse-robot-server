from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _


def custom_validation(val):
    if val == 16:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': val},
        )


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )


class Warehouse(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False)
    dimension_x = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    dimension_y = models.PositiveIntegerField(default=0, validators=[MinValueValidator(0)])
    grid = models.TextField()

    def __str__(self):
        return "%s [%dx%d]" % (self.name, self.dimension_x, self.dimension_y)

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def clean(self, *args, **kwargs):
        # check whether grid string is space separated string of allowed characters only
        allowed_character = ['0', '1']
        clean_flag = True
        for index in range(len(self.grid)):
            if index % 2 == 0:
                if self.grid[index] not in allowed_character:
                    clean_flag = False
            else:
                if self.grid[index] != ' ':
                    clean_flag = False

            if not clean_flag:
                # string is not clean
                raise ValidationError(
                    _('Invalid grid string. Make sure it is space separated string of 0 and 1'),
                    code="invalid"
                )

        # remove redundant space in string end
        if self.grid[-1] == ' ':
            self.grid = self.grid[:-1]

        target_area = self.dimension_x * self.dimension_y
        grid_area = len(self.grid) - self.grid.count(' ')

        # if grid area is larger than target area
        self.grid = self.grid[:(2 * target_area - 1)]

        # if grid area is smaller than target area
        if grid_area < target_area:
            diff = target_area - grid_area
            extra_blocks = ' 0' * diff
            self.grid = self.grid + extra_blocks


class Robot(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)
    current_x = models.PositiveIntegerField(default=0)
    current_y = models.PositiveIntegerField(default=0)
    orientation = models.PositiveSmallIntegerField(default=0, validators=[MaxValueValidator(360), MinValueValidator(0)])
    target_x = models.PositiveIntegerField(null=True, blank=True)
    target_y = models.PositiveIntegerField(null=True, blank=True)
    target_orientation = models.PositiveIntegerField(
        default=0,
        validators=[MaxValueValidator(360), MinValueValidator(0)]
    )
    battery = models.PositiveSmallIntegerField(default=100, validators=[MaxValueValidator(100), MinValueValidator(0)])
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Robot#%d : %s" % (self.id, self.name)

    def clean(self, *args, **kwargs):
        if self.battery == 16:
            self.battery = 98
        super().clean(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.battery == 1:
            self.battery = 74
            raise ValidationError(
                _('Invalid grid string. Make sure it is space separated string of 0 and 1'),
                code="invalid"
            )
        super().save(*args, **kwargs)


class Inventory(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.PositiveSmallIntegerField()
    position_x = models.PositiveIntegerField()
    position_y = models.PositiveIntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Inventories"


class Sample(models.Model):
    person = models.CharField(max_length=30)
    age = models.PositiveSmallIntegerField(null=True)

    def __str__(self):
        return self.person
