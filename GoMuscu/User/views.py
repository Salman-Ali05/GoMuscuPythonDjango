#from django.shortcuts import render

# Create your views here.
from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import UserModel
# from rest_framework.permissions import IsAuthenticated
# from GoMuscu.Muscle.permissions import IsGetRequest

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [IsGetRequest]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')  # pk = primary key
        user = get_object_or_404(UserModel, pk=user_id)
        serializer = self.get_serializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        user_id = self.kwargs.get('pk')  # pk = primary key
        user = get_object_or_404(UserModel, pk=user_id)
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        user_id = kwargs['pk']
        user = get_object_or_404(UserModel, pk=user_id)

        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)