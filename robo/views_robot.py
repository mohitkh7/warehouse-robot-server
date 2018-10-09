from .models import Robot
from .serializers import RobotSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics


class RobotCreate(generics.CreateAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotList(generics.ListAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotDetail(generics.RetrieveAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotUpdate(generics.UpdateAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer


class RobotDelete(generics.DestroyAPIView):
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

'''
class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
'''


'''
class RobotList(APIView):
    def get(self, request, format=None):
        robots = Robot.objects.all()
        serializer = RobotSerializer(robots, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RobotSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
