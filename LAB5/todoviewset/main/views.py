from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from main.models import Todo
from .serializers import TodoSerializer

from rest_framework import viewsets

from .serializers import TodoSerializer

class TodoViewSet(viewsets.ViewSet):
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = Todo.objects.all()
        serializer = TodoSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Todo.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = TodoSerializer(user)
        return Response(serializer.data)

class TodoViewSetComplete(viewsets.ModelViewSet):
    # permission_classes = (AllowAny,)
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.filter(completed=True)
    serializer_class = TodoSerializer

class TodoViewSet2(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


# class DetailTodo(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthenticated,)
#
#     queryset = Todo.objects.all()
#     serializer_class = TodoSerializer