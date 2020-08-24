from django.urls import path, include
from django.conf.urls import url, include
from rest_framework import routers, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.schemas import get_schema_view

API_TITLE = 'Blog API'
API_DESCRIPTION = 'A Web API for creating and editing blog posts.'


@api_view(['GET', 'POST'])
@permission_classes((permissions.AllowAny,))
def hello_world(request):
    if request.method == 'POST':
        return Response({"message": "Got some data!", "data": request.data})
    return Response({"message": "Hello, world! from django"})


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()

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
    url(r'^docs/$', schema_view),
]
