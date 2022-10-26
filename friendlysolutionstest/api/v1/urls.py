from rest_framework import routers
from friendlysolutionstest.api.v1.views import ImageViewSet

router = routers.SimpleRouter()
router.register(r'image', ImageViewSet)
urlpatterns = router.urls
