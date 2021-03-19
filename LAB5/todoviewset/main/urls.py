from rest_framework.routers import DefaultRouter
from .views import TodoViewSet, TodoViewSet2, TodoViewSetComplete
router = DefaultRouter()
router.register(r'todos-list', TodoViewSet, basename='user')
router.register(r'todos-cre-del-patch-get', TodoViewSet2, basename='get')
router.register(r'todos/complete', TodoViewSetComplete, basename='complete')

urlpatterns = router.urls


"""
from django.urls import path

from .views import TodoViewSet
from rest_framework.routers import DefaultRouter

app_name = "main"
urlpatterns = [
    path('todos-list/', TodoViewSet.as_view({'get': 'list'})),
    path('todos-list/<int:pk>', TodoViewSet.as_view({'get': 'retrieve'})),
]
"""


# from django.urls import path
#
# from .views import TodoViewSet2
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register('todos-list/', TodoViewSet2, basename='todos')
# urlpatterns = router.urls

