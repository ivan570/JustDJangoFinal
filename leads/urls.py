from django.contrib import admin
from django.urls import path
from .views import (
    lead_list, lead_details, lead_create,lead_update, lead_delete,
    LeadListView, LeadDetailView, LeadCreateView, LeadUpdateView, LeadDeleteView
)

urlpatterns = [
    path('', LeadListView.as_view(), name='lead-list'),
    # <pk> should match with funcation argument name
    path('create/', LeadCreateView.as_view(), name='lead-create'),
    path('<int:pk>/', LeadDetailView.as_view(), name='lead-details'),
    path('<int:pk>/update/', LeadUpdateView.as_view(), name='lead-update'),
    path('<int:pk>/delete/', LeadDeleteView.as_view(), name='lead-delete'),

]
