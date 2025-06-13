from django.contrib import admin
from .models import Challenge, Question, Submission

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

@admin.register(Challenge)
class ChallengeAdmin(admin.ModelAdmin):
    list_display = ("name", "type", "difficulty")
    inlines = [QuestionInline]

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ("text", "challenge", "correct_answer")

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ("user", "challenge", "score", "submitted_at")
    list_filter = ("challenge", "user")