from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.authentication import BasicAuthentication
from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="Codeme API",
      default_version='v1',
      description="Code API Documentation",
      terms_of_service="https://www.github.com/h4medrostami/Kirpi",
      contact=openapi.Contact(email="seydali.zewia@gmail.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   authentication_classes=(BasicAuthentication,),
#    permission_classes=(permissions.IsAuthenticated,),
   permission_classes=[permissions.AllowAny],
)