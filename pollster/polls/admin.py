from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Django App"
admin.site.site_title = "Django App Area"
admin.site.index_title = "Welcome to this Django App"


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {"fields": ["question_text"]}), ("Date Information", {
        "fields": ["pub_date"], "classes":["collapse"]}), ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
