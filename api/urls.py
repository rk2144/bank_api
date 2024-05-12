from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BankViewSet, BranchViewSet, AccountViewSet

router = DefaultRouter()
router.register(r'banks', BankViewSet)
router.register(r'branches', BranchViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('home/', include(router.urls)),
    
]
