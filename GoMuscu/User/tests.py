# from django.test import TestCase
# from rest_framework.test import APIClient
# from rest_framework import status
# from .models import UserModel

# class UserViewSetTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()

#     def test_create_user(self):
#         data = {
#             "userName": "New User",
#             "password": "Password123"
#         }

#         response = self.client.post('/user/', data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#         user = UserModel.objects.get(userName="New User")
#         self.assertEqual(user.userName, "New User")

#     def test_retrieve_user(self):
#         # Créez un objet UserModel pour le récupérer
#         user = UserModel.objects.create(userName="Test User", password="TestPassword")

#         response = self.client.get(f'/user/{user.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['userName'], "Test User")

#     def test_partial_update_user(self):
#         # Créez un objet UserModel pour le mettre à jour partiellement
#         user = UserModel.objects.create(userName="Original User", password="OriginalPassword")

#         data = {
#             "userName": "Updated User"
#         }

#         response = self.client.patch(f'/user/{user.id}/', data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#         user.refresh_from_db()
#         self.assertEqual(user.userName, "Updated User")

#     def test_delete_user(self):
#         # Créez un objet UserModel pour le supprimer
#         user = UserModel.objects.create(userName="To Be Deleted", password="ToDelete123")

#         response = self.client.delete(f'/user/{user.id}/')
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

#         # Assurez-vous que l'utilisateur a été supprimé de la base de données
#         with self.assertRaises(UserModel.DoesNotExist):
#             UserModel.objects.get(id=user.id)
