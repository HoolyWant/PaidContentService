from django.urls import path

from content_app.apps import ContentAppConfig
from content_app.views import ChannelView, ChannelList, home, ChannelCreate

app_name = ContentAppConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('channels/', ChannelList.as_view(), name='channel_list'),
    path('channels/<int:pk>', ChannelView.as_view(), name='channel_view'),
    path('channels/create/', ChannelCreate.as_view(), name='channel_create'),
]
