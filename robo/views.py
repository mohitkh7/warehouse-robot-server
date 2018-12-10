from django.http import JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Warehouse
from .serializers import WarehouseSerializer


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


@api_view(['POST'])
def create_warehouse(request):
    """
    :param request:
    :param POST: (required) name, dimension_x, dimension_y, grid
    :return: 400 if incorrect parameters are sent or database request fails
    :return: 201 successful
    """
    name = request.POST.get('name', None)
    dimension_x = request.POST.get('dimension_x', None)
    dimension_y = request.POST.get('dimension_y', None)
    grid = request.POST.get('grid', None)

    if not name or not dimension_x or not dimension_y or not grid:
        # incorrect request received
        error_message = "Missing parameters in request. Send name, dimension_x, dimension_y, grid"
        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)

    try:
        warehouse = Warehouse(
            name=name,
            dimension_x=dimension_x,
            dimension_y=dimension_y,
            grid=grid
        )
        warehouse.save()
    except Exception as e:
        error_message = str(e)
        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
    return Response("Warehouse successfully created", status=status.HTTP_201_CREATED)


@api_view(['GET'])
def get_warehouse(request, wid):
    """
    :param request:
    :param wid: warehouse id
    :return: 404 if warehouse instance does not exist
    :return: 200 successful
    """
    try:
        warehouse = Warehouse.objects.get(id=wid)

    except Warehouse.DoesNotExist:
        error_msg = "Warehouse does not exist. Incorrect id"
        return Response(error_msg, status=status.HTTP_404_NOT_FOUND)

    serializer = WarehouseSerializer(warehouse)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_warehouse_list(request):
    """
    Return list of all warehouse name
    :param request:
    :return: 404 if database request fails
    :return: 200 successful
    """
    try:
        warehouses = Warehouse.objects.all()

    except Exception as e:
        error_msg = str(e)
        return Response(error_msg, status=status.HTTP_404_NOT_FOUND)

    serializer = WarehouseSerializer(warehouses, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def update_warehouse(request, wid):
    """
    :param request:
    :param wid: warehouse ID
    :param POST: (optional) name, dimension_x, dimension_y, grid
    :return: 400 if incorrect parameters are sent or database request fails
    :return: 201 successful
    """
    name = request.POST.get('name', None)
    dimension_x = request.POST.get('dimension_x', None)
    dimension_y = request.POST.get('dimension_y', None)
    grid = request.POST.get('grid', None)

    try:
        warehouse = Warehouse.objects.get(id=wid)
        if name:
            warehouse.name = name
        if dimension_x:
            warehouse.dimension_x = dimension_x
        if dimension_y:
            warehouse.dimension_y = dimension_y
        if grid:
            warehouse.grid = grid
        warehouse.save()  # save the updates

    except Warehouse.DoesNotExist:
        error_msg = "Warehouse does not exist. Incorrect id"
        return Response(error_msg, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        print(str(e))
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    msg = "Warehouse details successfully updated"
    return Response(msg, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def delete_warehouse(request, wid):
    """
    Remove a warehouse
    :param request:
    :param wid: URL parameter warehouse id
    :return: 404 if warehouse instance does not exist
    :return: 200 successful
    """
    try:
        warehouse = Warehouse.objects.get(id=wid)
        warehouse.delete()

    except Warehouse.DoesNotExist:
        error_msg = "Warehouse does not exist. Incorrect id"
        return Response(error_msg, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    return Response("Warehouse successfully deleted.", status=status.HTTP_204_NO_CONTENT)
