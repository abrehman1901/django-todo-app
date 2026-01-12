from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_http_methods
from .models import Task


def signup(request):
    if request.user.is_authenticated:
        return redirect("task_list")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "registration/signup.html", {"form": form})


@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user).order_by("-created_at")
    total = tasks.count()
    done_count = tasks.filter(completed=True).count()
    pending_count = total - done_count

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            Task.objects.create(user=request.user, title=title)
        return redirect("task_list")

    return render(
        request,
        "todo/task_list.html",
        {
            "tasks": tasks,
            "total": total,
            "done_count": done_count,
            "pending_count": pending_count,
        },
    )


@require_POST
@login_required
def toggle_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect("task_list")


@require_POST
@login_required
def delete_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.delete()
    return redirect("task_list")


@require_POST
@login_required
def clear_completed(request):
    Task.objects.filter(user=request.user, completed=True).delete()
    return redirect("task_list")


@require_http_methods(["GET", "POST"])
@login_required
def edit_task(request, pk):
    task = get_object_or_404(Task, pk=pk, user=request.user)

    if request.method == "POST":
        title = request.POST.get("title", "").strip()
        if title:
            task.title = title
            task.save()
        return redirect("task_list")

    return render(request, "todo/edit_task.html", {"task": task})
