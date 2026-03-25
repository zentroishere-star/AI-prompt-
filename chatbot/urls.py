from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('api/enhance/', views.enhance_prompt_api, name='enhance_api'),
    path('history/', views.history_view, name='history'),
    path('query/<int:query_id>/', views.query_detail_view, name='query_detail'),
    path('feedback/', views.feedback_view, name='feedback'),
    path('api/feedbacks/', views.get_positive_feedbacks, name='get_feedbacks'),
]

