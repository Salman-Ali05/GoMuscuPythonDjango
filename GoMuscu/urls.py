from django.urls import include, path
from rest_framework import routers
from GoMuscu.Exercice import views as gomuscu_views_exercice
from GoMuscu.Muscle import views as gomuscu_views_Muscle
from GoMuscu.User import views as gomuscu_views_User
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="GoMuscu API",
        default_version="v1"
    ),
    public=True,
)


router = routers.DefaultRouter()

router.register(r'exercice', gomuscu_views_exercice.ExerciceViewSet)
router.register(r'muscle', gomuscu_views_Muscle.MuscleViewSet)
router.register(r'user', gomuscu_views_User.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui')
]
