from django.shortcuts import render, redirect
from .forms import FeedbackForm
# from django.contrib import messages


def feedback_new(request):
    if request.method == 'POST':
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Your feedback have been submitted. Thanks for your time.")
            return redirect('feedback:success')
    form = FeedbackForm()

    context = {
        'form': form,
    }
    return render(request, 'feedback/form.html', context)
    

def feedback_success(request):
    return render(request, 'feedback/success.html')