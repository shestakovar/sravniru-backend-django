from django.urls import path, include
from rest_framework import routers
from .views import ProposalApiView

router = routers.DefaultRouter()
router.register(r'proposals', ProposalApiView)

urlpatterns = [
    path('', include(router.urls)),
]
