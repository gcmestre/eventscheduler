from django.urls import path

from . import views

app_name = 'events'
urlpatterns = [
    path('', views.EventList.as_view(), name='list'),
    path('create', views.EventCreate.as_view(), name='create'),
    path('<int:pk>/', views.EventDetail.as_view(), name='detail'),
    path('<int:pk>/update', views.EventUpdate.as_view(), name='update'),
    path('<int:pk>/subscribe', views.EventSubscribe.as_view(), name='subscribe'),
    path('<int:pk>/unsubscribe', views.EventUnsubscribe.as_view(), name='unsubscribe')
]