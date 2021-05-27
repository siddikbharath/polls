from django.contrib import admin
from .models import Question, Choice
# Register your models here.

class ChoiceInline(admin.TabularInline): # to display as tabular form
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]

    list_display = ('question_text', 'pub_date', 'was_published_recently') # to display as list
    list_filter = ['pub_date'] # to add the filter
    search_fields = ['question_text'] # to add search bar

admin.site.register(Question, QuestionAdmin)