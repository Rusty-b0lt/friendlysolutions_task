from django.urls import path, include
from rest_framework import routers

router = routers.DefaultRouter()

urlpatterns = router.urls + [
    path('v1/', include('friendlysolutionstest.api.v1.urls'), name='v1'),
]