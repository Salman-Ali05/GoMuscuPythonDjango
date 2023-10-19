# Create your views here.


from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import MuscleSerializer
from .models import MuscleModel
from rest_framework.permissions import IsAuthenticated
from .permissions import IsGetRequest



class MuscleViewSet(viewsets.ModelViewSet):
    queryset = MuscleModel.objects.all()
    serializer_class = MuscleSerializer

    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [IsGetRequest]
        else:
            permission_classes = [IsAuthenticated]
        return [permission() for permission in permission_classes]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, *args, **kwargs):
        muscle_id = self.kwargs.get('pk')  # pk = primary key
        muscle = get_object_or_404(MuscleModel, pk=muscle_id)
        serializer = self.get_serializer(muscle)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        muscle_id = self.kwargs.get('pk')  # pk = primary key
        muscle = get_object_or_404(MuscleModel, pk=muscle_id)
        serializer = self.get_serializer(muscle, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        muscle_id = kwargs['pk']
        muscle = get_object_or_404(MuscleModel, pk=muscle_id)

        muscle.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
