from django.urls import path, include
from django.conf.urls import url, include
from rest_framework import routers, permissions, serializers, viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.schemas import get_schema_view
from django.contrib.auth.models import User
from django.conf import settings
from django.conf.urls.static import static
# Serializers define the API representation.


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world! from django"})


schema_view = get_schema_view(
    title=API_TITLE,
    description=API_DESCRIPTION,
)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^hello/$', hello_world),
    path('api/company/', include('company.urls')),
    path('api/admin/', include('admins.urls')),
    path('api/', include('default.urls')),
    url(r'^docs/$', schema_view),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
