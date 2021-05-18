from rest_framework import routers
from core.api import viewsets


router = routers.DefaultRouter()

router.register("polls", viewsets.PollViewSet, basename='polls')
