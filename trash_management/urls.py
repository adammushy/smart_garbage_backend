from django.urls import path
from .views import *
app_name = 'trash_management'

urlpatterns = [
     path('trashbin-view',TrashBinView.as_view()),
     path('report-view',ReportView.as_view()),
     path('complain-view', ComplainView.as_view())
]
