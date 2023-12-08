from django.contrib import admin

from content_app.models import Channel, Publication


@admin.register(Channel)
class ChannelAdmin(admin.ModelAdmin):
    list_display = ['title', ]


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title', ]

