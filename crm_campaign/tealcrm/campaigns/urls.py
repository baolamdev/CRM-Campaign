from django.urls import path

from . import views

# app_name = 'campaigns'

urlpatterns = [
    path('', views.CampaignListView.as_view(), name='campaigns'),
    path('<int:pk>/', views.CampaignDetailView.as_view(), name='campaign_detail'),
    path('add/', views.CampaignCreateView.as_view(), name='campaign_add'),
    path('<int:pk>/edit/', views.CampaignEditView.as_view(), name='campaign_edit'),
    path('<int:pk>/edit/recipients/', views.CampaignEditRecipientsView.as_view(), name='campaign_edit_recipients'),
    path('<int:pk>/edit/from/', views.CampaignEditFromView.as_view(), name='campaign_edit_from'),
    path('<int:pk>/edit/subject/', views.CampaignEditSubjectView.as_view(), name='campaign_edit_subject'),
    path('<int:pk>/edit/content/', views.campaign_edit_content, name='campaign_edit_content'),
    path('<int:pk>/edit/content/template/', views.CampaignEditTemplateView.as_view(), name='campaign_edit_template'),
    path('<int:pk>/preview-email/', views.campaign_preview_email, name='campaign_preview_email'),
    path('<int:pk>/send/', views.send_campaign, name='send_campaign'),
    path('<int:pk>/send/done/', views.SendCampaignCompleteView.as_view(), name='send_campaign_complete'),
    path('<int:pk>/delete/', views.CampaignDeleteView.as_view(), name='delete_campaign'),
    path('<int:pk>/reports/', views.CampaignReportsView.as_view(), name='campaign_reports'),
    path('ajax/load-list-tags/', views.load_list_tags, name='load_list_tags'),
]
