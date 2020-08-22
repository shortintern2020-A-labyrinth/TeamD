from django.urls import path, include
from django.conf.urls import url, include
from django.contrib.auth.models import User
from rest_framework import serializers, viewsets, routers, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from company import views as company_views

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

@api_view(['GET','POST'])
@permission_classes((permissions.AllowAny,))
def hello_world(request):
        if request.method == 'POST':
                return Response({"message": "Got some data!", "data": request.data})
        return Response({"message": "Hello, world! from django"})

# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^hello/$', hello_world),
    path('api/company/', include('company.urls'))
]
