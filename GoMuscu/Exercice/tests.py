# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import ExerciceModel
# from .models import MuscleModel

# class ExerciceViewSetTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#     def test_create_exercice(self):
#         # Créez un objet MuscleModel pour l'utiliser dans le test
#         muscle = MuscleModel.objects.create(muscleName="Muscle 1")

#         data = {
#             "name": "New Exercice",
#             "desc": "New Description",
#             "idMuscle": muscle.id
#         }

#         response = self.client.post('/exercice/', data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         exercice = ExerciceModel.objects.get(name="New Exercice")
#         self.assertEqual(exercice.name, "New Exercice")

#     def test_retrieve_exercice(self):
#         # Créez un objet ExerciceModel pour le récupérer
#         muscle = MuscleModel.objects.create(muscleName="Muscle 1")
#         exercice = ExerciceModel.objects.create(name="Test Exercice", desc="Test Description", idMuscle=muscle)

#         response = self.client.get(f'/exercice/{exercice.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['name'], "Test Exercice")

#     def test_partial_update_exercice(self):
#         # Créez un objet ExerciceModel pour le mettre à jour partiellement
#         muscle = MuscleModel.objects.create(muscleName="Muscle 1")
#         exercice = ExerciceModel.objects.create(name="Original Name", desc="Original Description", idMuscle=muscle)

#         data = {
#             "name": "Updated Name"
#         }

#         response = self.client.patch(f'/exercice/{exercice.id}/', data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         exercice.refresh_from_db()
#         self.assertEqual(exercice.name, "Updated Name")

#     def test_delete_exercice(self):
#         # Créez un objet ExerciceModel pour le supprimer
#         muscle = MuscleModel.objects.create(muscleName="Muscle 1")
#         exercice = ExerciceModel.objects.create(name="To Be Deleted", desc="Description", idMuscle=muscle)

#         response = self.client.delete(f'/exercice/{exercice.id}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#         # Assurez-vous que l'exercice a été supprimé de la base de données
#         with self.assertRaises(ExerciceModel.DoesNotExist):
#             ExerciceModel.objects.get(id=exercice.id)
