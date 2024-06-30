from django.urls import path
from . import views
from .views import ServiceListView
from .views import (
    UserListView, UserDetailView,
    ServiceListView, ServiceDetailView,
    CreateSubscriptionView
)

urlpatterns = [
    path('users/', UserListView.as_view(), name='user_list'),
    path('users/<int:pk>/', UserDetailView.as_view(), name='user_detail'),
   path('services/', ServiceListView.as_view(), name='service_list'),
    path('services/<str:type>/', ServiceDetailView.as_view(), name='service_detail'),
    path('subscription/', CreateSubscriptionView.as_view(), name='create_subscription'),
]