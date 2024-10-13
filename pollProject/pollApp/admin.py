from django.contrib import admin
from .models import Question, Choice

admin.site.site_header = "Admin Page"
admin.site.site_title = "Voting Creation Portal"
admin.site.index_title = "Welcome to Voting Admin Area"

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 3
class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [(None, {'fields':['question_text']}), ('Date Information', {'fields': ['pub_date'], 'classes':['collapse']}),]
    inlines = [ChoiceInLine]

admin.site.register(Question, QuestionAdmin)