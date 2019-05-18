from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .forms import UserForm, UserProfileInfoForm
from django.contrib.auth import authenticate, login, logout, password_validation
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .models import Subject, Membership, UserProfileInfo
from django.db.models import Sum
from django.contrib import messages
from django.core.mail import send_mail
import random, string

# Create your views here.
def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            g_username = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
            g_password = ''.join(random.choices(string.ascii_letters + string.digits, k=9))
            send_mail(
                'Use This username and password',
                f"Your username= {g_username} and password= {g_password}.",
                'yalanotlobiti@gmail.com',
                [user.email],
                fail_silently=False,
            )
            user.set_password(g_password)
            user.username = g_username
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            return redirect('accounts:user_login')
        else:
            context = {'user_form': user_form, 'profile_form': profile_form}
            return render(request, 'accounts/register.html', context)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
        context = {'user_form': user_form, 'profile_form':profile_form}
        return render(request,'accounts/register.html', context)


@login_required
def user_logout(request):
    logout(request)
    return redirect('accounts:user_login')

@login_required
def dashboard(request, semester):
    subjects = Subject.objects.filter(user=request.user, membership__semester=semester)
    all_subjects = Subject.objects.all()
    other_semester = 'second' if semester == 'first' else 'first'
    subjects_other_semester = Subject.objects.filter(user=request.user, membership__semester=other_semester)
    context = {
        'all_subjects': all_subjects,
        'subjects': subjects,
        'semester': semester,
        'subjects_other_semester': subjects_other_semester,
        'other_semester': other_semester
    }
    return render(request, 'accounts/dashboard.html', context)


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            print(user)
            if user.is_active:
                login(request, user)
                return redirect('accounts:dashboard', semester='first')
            else:
                return HttpResponse("Your account was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")

    else:
        return render(request, 'accounts/login.html', {})


def remove_subject(request, subject_id, semester):
    user = request.user
    subject = Subject.objects.get(pk=subject_id)
    m = Membership.objects.filter(user=user, subject=subject, semester=semester)
    m.delete()
    return redirect('accounts:dashboard', semester=semester)

def add_subject(request, subject_id, semester):
    reached = Subject.objects.filter(user=request.user, membership__semester=semester).aggregate(total=Sum('hours'))
    hours = 0
    if reached['total']:
        hours = reached['total']
    if hours >= 50:
        messages.error(request, "You have reached your limits for this semester  ")
        return redirect('accounts:dashboard', semester=semester)
    sub = Subject.objects.get(pk=subject_id)
    user = request.user
    Membership.objects.create(user=user, subject=sub, semester=semester)
    return redirect('accounts:dashboard', semester=semester)


