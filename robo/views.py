from django.http import HttpResponse, JsonResponse
from .models import Robot, Warehouse


# Create your views here.
def index(request):
    response = JsonResponse(
        {'st': "On Gang Ganpataye Namah"}
    )
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response


def warehouse_details(request, wid):
    w = Warehouse.objects.get(id=wid)
    response = JsonResponse({
        'name': w.name,
        'x': w.dimension_x,
        'y': w.dimension_y,
        'grid': w.grid,

    })
    response["Access-Control-Allow-Origin"] = "*"
    response["Access-Control-Allow-Methods"] = "GET, OPTIONS"
    response["Access-Control-Max-Age"] = "1000"
    response["Access-Control-Allow-Headers"] = "X-Requested-With, Content-Type"
    return response


def create(request):
    robo_name = request.GET.get('name')
    r = Robot(name=robo_name)
    r.save()
    return HttpResponse("Robot created")
