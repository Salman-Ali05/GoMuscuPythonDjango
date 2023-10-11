from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExerciceSerializer
from .models import ExerciceModel
from rest_framework.permissions import IsAuthenticated
from .permissions import IsGetRequest


class ExerciceViewSet(viewsets.ModelViewSet):
    queryset = ExerciceModel.objects.all()
    serializer_class = ExerciceSerializer
    permission_classes = [IsAuthenticated]

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
        exercice_id = self.kwargs.get('pk')  # pk = primary key
        exercice = get_object_or_404(ExerciceModel, pk=exercice_id)
        serializer = self.get_serializer(exercice)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def partial_update(self, request, *args, **kwargs):
        exercice_id = self.kwargs.get('pk')  # pk = primary key
        exercice = get_object_or_404(ExerciceModel, pk=exercice_id)
        serializer = self.get_serializer(exercice, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        exercice_id = kwargs['pk']
        exercice = get_object_or_404(ExerciceModel, pk=exercice_id)

        exercice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
