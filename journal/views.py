from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Entry

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def entry_list(request):
    entries = Entry.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'journal/entry_list.html', {
        'entries': entries
    })

@login_required
def create_entry(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']

        Entry.objects.create(
            user=request.user,
            title=title,
            content=content
        )

        return redirect('entry_list')

    return render(request, 'journal/create_entry.html')

@login_required
def entry_detail(request, id):
    entry = get_object_or_404(Entry, id=id, user=request.user)

    return render(request, 'journal/entry_detail.html', {
        'entry': entry
    })

@login_required
def edit_entry(request, id):
    entry = get_object_or_404(Entry, id=id, user=request.user)

    if request.method == 'POST':
        entry.title = request.POST['title']
        entry.content = request.POST['content']
        entry.save()

        return redirect('entry_list')

    return render(request, 'journal/edit_entry.html', {
        'entry': entry
    })

@login_required
def delete_entry(request, id):
    entry = get_object_or_404(Entry, id=id, user=request.user)

    if request.method != 'POST':
        return redirect('entry_detail', id=entry.id)

    entry.delete()

    return redirect('entry_list')
