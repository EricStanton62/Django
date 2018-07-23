from django.contrib import admin

from .models import Question, Choice

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes':['collapse']}),
    ]
    inlines = [ChoiceInline]
    
admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
