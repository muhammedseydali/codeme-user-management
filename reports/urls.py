from django.urls import path
from .views import AdminReportViews, ManagerReportViews

urlpatterns = [
    path('admin/', AdminReportViews.as_view(), name='admin-report'),
    path('manager/', ManagerReportViews.as_view(), name='manager-report'),
]
