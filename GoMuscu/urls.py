from django.urls import include, path
from rest_framework import routers
from GoMuscu.Exercice import views as gomuscu_views_exercice
from GoMuscu.Muscle import views as gomuscu_views_Muscle
from GoMuscu.User import views as gomuscu_views_User
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


router = routers.DefaultRouter()

router.register(r'exercice', gomuscu_views_exercice.ExerciceViewSet)
router.register(r'muscle', gomuscu_views_Muscle.MuscleViewSet)
router.register(r'user', gomuscu_views_User.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh')
]
