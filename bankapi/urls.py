# urls.py in your_project_name

from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import BankViewSet, BranchViewSet, AccountViewSet

# Create a router and register your viewsets with it
router = routers.DefaultRouter()
router.register(r'banks', BankViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    
     # Add this line for DRF's authentication URLs
]
