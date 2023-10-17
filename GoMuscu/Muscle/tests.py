# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import MuscleModel

# class MuscleViewSetTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#     def test_create_muscle(self):
#         data = {
#             "muscleName": "New Muscle"
#         }

#         response = self.client.post('/muscle/', data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         muscle = MuscleModel.objects.get(muscleName="New Muscle")
#         self.assertEqual(muscle.muscleName, "New Muscle")

#     def test_retrieve_muscle(self):
#         muscle = MuscleModel.objects.create(muscleName="Test Muscle")

#         response = self.client.get(f'/muscle/{muscle.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['muscleName'], "Test Muscle")

#     def test_partial_update_muscle(self):
#         muscle = MuscleModel.objects.create(muscleName="Original Muscle")

#         data = {
#             "muscleName": "Updated Muscle"
#         }

#         response = self.client.patch(f'/muscle/{muscle.id}/', data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         muscle.refresh_from_db()
#         self.assertEqual(muscle.muscleName, "Updated Muscle")

#     def test_delete_muscle(self):
#         muscle = MuscleModel.objects.create(muscleName="To Be Deleted")

#         response = self.client.delete(f'/muscle/{muscle.id}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#         with self.assertRaises(MuscleModel.DoesNotExist):
#             MuscleModel.objects.get(id=muscle.id)
