from django.urls import path

from content_app.apps import ContentAppConfig
from content_app.views import ChannelView, ChannelList, home, ChannelCreate, sub_success, \
    PublicationView, SubChannelList, PublicationCreate, PublicationEdit, PublicationDelete

app_name = ContentAppConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('channels/', ChannelList.as_view(template_name='content_app/channel_list.html'), name='channel_list'),
    path('channels/<int:pk>', ChannelView.as_view(), name='channel_view'),
    path('channels/create/', ChannelCreate.as_view(), name='channel_create'),
    path('publication/<int:pk>', PublicationView.as_view(), name='publication_detail'),
    path('channels/success/', sub_success, name='success'),
    path('subscriptions/', SubChannelList.as_view(template_name='content_app/sub_channels.html'), name='sub_channels'),
    path('publication/create/', PublicationCreate.as_view(), name='publication_create'),
    path('publication/edit/<int:pk>', PublicationEdit.as_view(), name='publication_edit'),
    path('publication/delete/<int:pk>', PublicationDelete.as_view(), name='publication_delete'),
]
