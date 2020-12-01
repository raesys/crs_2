from django.shortcuts import render, get_object_or_404, redirect
from .forms import CamperForm
from accounts.forms import AddFundsForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Camper
from django.http import Http404

# Camp registration fee
registration_fee = 80

# Camp homepage
def home(request):
    return redirect('camper:list')


# Camper list
@login_required(login_url='accounts:login')
def camper_list(request):
    camper_list = request.user.campers.all()

    context = {
        'camper_list': camper_list,
        # 'query_list': camper_list,
    }
    return render(request, 'camper/list.html', context)


# Add new camper
# @login_required(login_url='accounts:login')
# def new_camper(request):
#     # Checking users balance
#     user_profile = request.user.profile
#     if user_profile.balance < registration_fee:
#         messages.info(request, f"Your current balance is GHS {user_profile.balance}, which is insufficient. Head over to your dashboard and top up!", extra_tags='alert-danger')
#         return redirect('camper:list')
#     if request.method == 'POST':
#         form = CamperForm(data=request.POST)
#         if form.is_valid():
#             camper = form.save(commit=False)
#             camper.created_by = request.user
#             camper.save()
#             user_profile.balance -= registration_fee
#             user_profile.save()
#             messages.success(request, f"{camper.first_name} {camper.last_name} has been successfully registered as a camper. Your balance is now GHS {user_profile.balance}.")
#             return redirect('camper:list')

#     form = CamperForm()

#     context = {
#         'form': form,
#     }
#     return render(request, 'camper/camper_form.html', context)


# Add new camper
@login_required(login_url='accounts:login')
def new_camper(request):
    # Checking users balance
    user_profile = request.user.profile
    if user_profile.balance < registration_fee:
        messages.info(request, f"Your current balance is GHS {user_profile.balance}, which is insufficient. Head over to your dashboard and top up!", extra_tags='alert-danger')
        return redirect('camper:list')
    camper = Camper(created_by=request.user)
    if request.method == 'POST':
        form = CamperForm(data=request.POST, instance=camper)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            user_profile.balance -= registration_fee
            user_profile.save()
            messages.success(request, f"{first_name} {last_name} has been successfully registered as a camper. Your balance is now GHS {user_profile.balance}.")
            return redirect('camper:list')
            
    form = CamperForm()

    context = {
        'form': form,
    }
    return render(request, 'camper/camper_form.html', context)

# Update an existing camper details
@login_required(login_url='accounts:login')
def update_camper(request, id):
    camper = get_object_or_404(Camper, pk=id)
    if camper.created_by != request.user:
        raise Http404
        return redirect('camper:list') # Not needed though
    if request.method == 'POST':
        form = CamperForm(data=request.POST, instance=camper)
        if form.is_valid():
            form.save()
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            messages.success(request, f"{first_name} {last_name} has been successfully updated.")
            return redirect('camper:list')
    form = CamperForm(instance=camper)

    context = {
        'form': form,
    }
    return render(request, 'camper/camper_form.html', context)


# Delete an existing camper
@login_required(login_url='accounts:login')
def delete_camper(request, id):
    camper = get_object_or_404(Camper, pk=id)
    if camper.created_by != request.user:
        raise Http404
        return redirect('camper:list') # Not needed though
    user_profile = request.user.profile
    first_name = camper.first_name
    last_name = camper.last_name
    if request.method == 'POST':
        camper.delete()
        user_profile.balance += registration_fee
        user_profile.save()
        messages.info(request, f"{first_name} {last_name} has been deleted as a camper. Your balance is now GHS {user_profile.balance}", extra_tags='alert-danger')
        return redirect('camper:list')
    raise Http404



# Campers Dashboard
@login_required(login_url='accounts:login')
def dashboard(request):
    user_profile = request.user.profile 
    user_campers = request.user.campers.all()
    genders = [g.gender for g in user_campers]
    gender_total = len(genders)
    gender_male = genders.count('M')
    gender_female = genders.count('F')

    if request.method == 'POST':
        form = AddFundsForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data.get('amount')
            user_profile.balance += amount
            user_profile.save()
            messages.success(request, f"You have successfully loaded your account with GHS {amount}. Your new balance is GHS {user_profile.balance}")
            return redirect('camper:dashboard')
    else:
        form = AddFundsForm()

    context = {
        'user_profile': user_profile,
        'gender_total': gender_total,
        'gender_male': gender_male,
        'gender_female': gender_female,
        'registration_fee': registration_fee,
        'form': form
    }
    return render(request, 'camper/dashboard.html', context)


