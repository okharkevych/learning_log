from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


def register(request):
    """Register a new user"""
    if request.method != 'POST':
        # Show an empty registration form
        form = UserCreationForm()
    else:
        # Process the filled in form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Authorize user and redirect to homepage
            login(request, new_user)
            return redirect('learning_logs:index')

    # Show an empty or invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
