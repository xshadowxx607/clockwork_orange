from django.db import models
from django.contrib.auth.models import User

class Challenge(models.Model):
    CHALLENGE_TYPES = [('PHIS', 'Phishing'), ('PRET', 'Pretexting'), ('BAIT', 'Baiting'), ('TAIL', 'Tailgating')]
    DIFFICULTY = [('E', 'Easy'), ('M', 'Medium'), ('H', 'Hard')]

    challenge_id = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=4, choices=CHALLENGE_TYPES)
    difficulty = models.CharField(max_length=1, choices=DIFFICULTY)

    def __str__(self):
        return self.name

class Question(models.Model):
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE, related_name="questions")
    text = models.TextField()
    choices = models.TextField(help_text="Each option on a new line.")
    correct_answer = models.TextField()

    def get_choice_list(self):
        return self.choices.splitlines()

    def __str__(self):
        return f"Question for {self.challenge.name}"

class Submission(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    challenge = models.ForeignKey(Challenge, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    submitted_at = models.DateTimeField(auto_now_add=True)
