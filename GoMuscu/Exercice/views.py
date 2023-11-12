from rest_framework.generics import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import ExerciceSerializer
from .models import ExerciceModel
from rest_framework.decorators import action
from rest_framework.decorators import api_view
# from rest_framework.permissions import IsAuthenticated
# from .permissions import IsGetRequest

class ExerciceViewSet(viewsets.ModelViewSet):
    queryset = ExerciceModel.objects.all()
    serializer_class = ExerciceSerializer

    # def get_permissions(self):
    #     if self.action == 'list':
    #         permission_classes = [IsGetRequest]
    #     else:
    #         permission_classes = [IsAuthenticated]
    #     return [permission() for permission in permission_classes]

    def create_exercice(self, request):
        # Votre logique de création d'exercice ici
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk=None):
        exercice = self.get_object()
        serializer = self.get_serializer(exercice, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        exercice = self.get_object()
        exercice.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    # Les méthodes retrieve et list sont accessibles publiquement
    # Vous n'avez pas besoin d'authentification pour ces méthodes
