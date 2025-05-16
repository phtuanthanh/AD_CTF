from django.shortcuts import render, redirect
from django.db import connection
from django.http import HttpResponse
import datetime
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def reset_competition(request):
    if request.method == "POST":
        with connection.cursor() as cursor:
            cursor.execute("TRUNCATE scoring_flag, scoring_capture, scoring_statuscheck, scoring_checkerstate,scoring_scoreboard RESTART IDENTITY CASCADE;")
        return HttpResponse("Đã xóa dữ liệu các bảng chính!")
    return render(request, "reset.html")

@staff_member_required
def update_competition_time(request):
    return redirect('/admin/scoring/gamecontrol/1/change/')