
from django.urls import path
from .views import (
	ExprecordListView,
	# ExprecordDetailView,
	ExprecordCreateView,
	# ExprecordUpdateView,
	# ExprecordDeleteView,
    UserExprecordListView,
)
from . import views

urlpatterns = [
    path('', views.home, name='exprecord-home'),
    path('records/', ExprecordListView.as_view(), name='exprecord-records'),
    # path('', views.home, name='exprecord-home'),
    # path('user/<str:username>/', UserExprecordListView.as_view(), name='user-exprecord'),
    # path('<int:pk>/', ExprecordDetailView.as_view(), name='exprecord-detail'),
    path('new/', ExprecordCreateView.as_view(), name='exprecord-create'),
    # path('<int:pk>/update/', ExprecordUpdateView.as_view(), name='exprecord-update'),
    # path('<int:pk>/delete/', ExprecordDeleteView.as_view(), name='exprecord-delete'),
    path('about/', views.about, name='exprecord-about'),
]