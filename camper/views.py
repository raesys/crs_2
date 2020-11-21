from django.shortcuts import render, get_object_or_404, redirect
from .forms import CamperForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Camper

# Camp registration fee
registration_fee = 0




def home(request):
    return render(request, 'camper/index.html')


# Camper list
# @login_required(login_url='accounts:login')
def camper_list(request):
    camper_list = request.user.campers.all()

    context = {
        'camper_list': camper_list,
        # 'query_list': camper_list,
    }
    return render(request, 'camper/list.html', context)


# Add new camper
# @login_required(login_url='accounts:login')
def new_camper(request):
    # Method 1
    # camper = Camper(created_by=request.user)
    if request.method == 'POST':
        # form = CamperForm(data=request.POST, instance=camper) # To support Method 1
        form = CamperForm(data=request.POST)
        if form.is_valid():
            # Method 2
            camper = form.save(commit=False)
            camper.created_by = request.user
            camper.save()
            # form.save()
            # first_name = camper.cleaned_data.get('first_name') # Not working because now camper is an object of Camper
            first_name = camper.first_name
            messages.success(request, f"{first_name} has been successfully registered as a camper.")
            return redirect('camper:list')
    else:
        form = CamperForm()

    context = {
        'form': form,
    }
    return render(request, 'camper/camper_form.html', context)


# Update an existing camper details
# @login_required(login_url='accounts:login')
def update_camper(request, id):
    camper = get_object_or_404(Camper, pk=id)
    if camper.created_by != request.user:
        messages.info(request, "You are not authorized to do this. This account has being logged for investigations", extra_tags='alert-danger')
        return redirect('camper:list')
    if request.method == 'POST':
        form = CamperForm(data=request.POST, instance=camper)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            messages.success(request, f"{first_name} has been successfully updated.")
            return redirect('camper:list')
    else:
        form = CamperForm(instance=camper)

    context = {
        'form': form,
    }
    return render(request, 'camper/camper_form.html', context)


# Delete an existing camper
# @login_required(login_url='accounts:login')
def delete_camper(request, id):
    camper = get_object_or_404(Camper, pk=id)
    if camper.created_by != request.user:
        messages.info(request, "You are not authorized to do this. This account has being logged for investigations", extra_tags='alert-danger')
        return redirect('camper:list')
    first_name = camper.first_name
    camper.delete()
    messages.info(request, f"{first_name} has been deleted as a camper.", extra_tags='alert-danger')
    return redirect('camper:list')
