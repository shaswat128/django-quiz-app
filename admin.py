from django.contrib import admin
from .models import Question, Choice, Submission, Lesson, Topic, Answer, Course

# Inline for Choice
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Inline for Question
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Question Admin
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text',)
    inlines = [ChoiceInline]

# Lesson Admin
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# Register models
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Topic)
admin.site.register(Answer)
admin.site.register(Course)
