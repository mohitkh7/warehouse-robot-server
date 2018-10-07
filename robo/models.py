from django.db import models


class Warehouse(models.Model):
    name = models.CharField(max_length=30, unique=True, null=False)
    dimension_x = models.IntegerField(default=0)
    dimension_y = models.IntegerField(default=0)
    grid = models.TextField()

    def __str__(self):
        return "%s [%dx%d]" % (self.name, self.dimension_x, self.dimension_y)


class Robot(models.Model):
    name = models.CharField(max_length=20, unique=True, null=False)
    current_x = models.IntegerField(default=0)
    current_y = models.IntegerField(default=0)
    orientation = models.IntegerField(default=0)
    target_x = models.IntegerField(null=True)
    target_y = models.IntegerField(null=True)
    target_orientation = models.IntegerField(default=0)
    battery = models.IntegerField(default=100)
    warehouse = models.ForeignKey(Warehouse, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "Robot#%d : %s" % (self.id, self.name)


class Inventory(models.Model):
    name = models.CharField(max_length=30)
    quantity = models.IntegerField()
    position_x = models.IntegerField()
    position_y = models.IntegerField()
    warehouse = models.ForeignKey(Warehouse, on_delete=models.CASCADE)
