
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import sqlite3
from datetime import datetime

DB = 'db.sqlite3'

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def index(request):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, type, difficulty FROM core_challenge")
    challenges = cursor.fetchall()
    conn.close()
    return render(request, 'core/index.html', {'challenges': challenges})

@login_required
def challenge_view(request, pk):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name FROM core_challenge WHERE id = ?", (pk,))
    challenge = cursor.fetchone()
    cursor.execute("SELECT id, text, choices, correct_answer FROM core_question WHERE challenge_id = ?", (pk,))
    questions = cursor.fetchall()

    if request.method == 'GET':
        request.session['start_time'] = datetime.now().timestamp()
        return render(request, 'core/challenge.html', {'challenge': challenge, 'questions': questions})

    elif request.method == 'POST':
        score = 0
        hint_penalty = 0
        start_time = request.session.get('start_time', datetime.now().timestamp())
        elapsed_seconds = int(datetime.now().timestamp() - start_time)
        time_penalty = elapsed_seconds // 10  # 1 point per 10 seconds

        for q in questions:
            user_answer = request.POST.get(f"q{q[0]}", "").strip()
            hint_used = request.POST.get(f"hint_used_{q[0]}", "0") == "1"
            correct = q[3].strip()
            if user_answer.lower() == correct.lower():
                score += 10
            if hint_used:
                hint_penalty += 5

        final_score = max(0, score - time_penalty - hint_penalty)
        cursor.execute("INSERT INTO core_submission (user, challenge_id, score, submitted_at) VALUES (?, ?, ?, ?)",
                       (request.user.username, pk, final_score, datetime.now()))
        conn.commit()
        conn.close()
        return render(request, 'core/result.html', {
            'challenge': challenge,
            'score': score,
            'final_score': final_score,
            'time_penalty': time_penalty,
            'hint_penalty': hint_penalty,
            'elapsed': elapsed_seconds
        })

def leaderboard(request):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("SELECT user, SUM(score) FROM core_submission GROUP BY user ORDER BY SUM(score) DESC")
    results = cursor.fetchall()
    conn.close()
    return render(request, 'core/leaderboard.html', {'leaderboard': results})

@login_required
def profile_view(request):
    conn = sqlite3.connect(DB)
    cursor = conn.cursor()
    cursor.execute("""
        SELECT s.id, c.name, s.score, s.submitted_at
        FROM core_submission s
        JOIN core_challenge c ON s.challenge_id = c.id
        WHERE s.user = ?
        ORDER BY s.submitted_at DESC
    """, (request.user.username,))
    submissions = cursor.fetchall()
    conn.close()
    return render(request, 'core/profile.html', {'submissions': submissions})
