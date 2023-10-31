from django.urls import path
from django.conf.urls.static import static
from .views import CustomUserDetailView, CustomUserListView, CustomUserLoginView, LocationListCreateView, TemperatureDetailView, TemperatureListView
from .views import LocationDetailView
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import LocationListCreateView,LocationDetailView
from django.conf import settings
from django.urls import path
from api.views import DeviceListAPIView, DeviceDetailView, FlowrateListAPIView, FlowrateDetailView





schema_view= get_schema_view(
    openapi.Info(
        title="Locations API",
        description='API for Locations',
        default_version ='v1',),
        public=True,
        permission_classes=(permissions.AllowAny,),
    )


urlpatterns = [
    path('devices/', DeviceListAPIView.as_view(), name='device-list'),
    path('devices/<int:id>/', DeviceDetailView.as_view(), name='device-detail'),
    path('flowrate/', FlowrateListAPIView.as_view(), name='flowrate-list'),
    path('flowrate/<int:id>/', FlowrateDetailView.as_view(), name='flowrate-detail'),
    path('locations/', LocationListCreateView.as_view(), name='location-list-create'),
    path('locations/<int:pk>/', LocationDetailView.as_view(), name='location-detail'),
    path('document/locations',schema_view.with_ui('swagger',cache_timeout=0),name='schema-swagger-ui'),
    path("Temperature/", TemperatureListView.as_view(), name="temperature_list_view"),
    path("Temperature/<int:id>/", TemperatureDetailView.as_view(), name="temperature_detail_view"),
    path('user/', CustomUserListView.as_view(), name='user-list-create'),
    path('user/<int:pk>/', CustomUserDetailView.as_view(), name='user-detail-view'),
    path('login/', CustomUserLoginView.as_view(), name='user-login'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)


