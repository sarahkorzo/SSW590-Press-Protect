from django.urls import path
from . import views

urlpatterns = [
    path('admin-dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('editor-dashboard/', views.editor_dashboard, name='editor-dashboard'),
    path('marketer-dashboard/', views.marketer_dashboard, name='marketer-dashboard'),
    path('viewer-dashboard/', views.viewer_dashboard, name='viewer-dashboard'),
]
