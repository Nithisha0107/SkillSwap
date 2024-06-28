from rest_framework.routers import DefaultRouter
from .views import CategoryViewset,SkillViewSet

router = DefaultRouter()

router.register(r'category',CategoryViewset,basename='category')
router.register(r'skill',SkillViewSet,basename='skill')

urlpatterns = []+router.urls