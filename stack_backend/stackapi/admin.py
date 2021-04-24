from django.contrib import admin
from .models import Question


class QuestionsAdmin(admin.ModelAdmin):
    list_display = [
        "question",
        "votes",
        "views",
        "tags"
    ]


admin.site.register(Question)
