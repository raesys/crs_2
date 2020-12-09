from django.contrib import admin
from .models import Feedback


class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('category', 'comments')
    list_filter = ('category',)


admin.site.register(Feedback, FeedbackAdmin)
