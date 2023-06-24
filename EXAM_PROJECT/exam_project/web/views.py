from django.shortcuts import render, redirect
from exam_project.web.models import Profile, Fruit
from exam_project.web.forms import *


def index_page(request):
    profile = Profile.objects.all().first()

    context = {
        "profile": profile
    }

    return render(request, 'core and other/index.html', context)


def dashboard_page(request):
    profile = Profile.objects.all().first()
    fruits = Fruit.objects.all()

    print(fruits)

    context = {
        "profile": profile,
        "fruits": fruits
    }

    return render(request, 'core and other/dashboard.html', context)


def fruit_create_page(request):
    form = AddFruitModelForm()
    profile = Profile.objects.all().first()

    if request.method == "POST":
        form = AddFruitModelForm(request.POST)
        if form.is_valid():
            album = form.save(commit=False)  # new
            album.profile = profile  # new
            form.save()  # new
            return redirect('dashboard page')

    context = {
        "form": form,
        "profile": profile
    }

    return render(request, 'fruits/create-fruit.html', context)


def fruit_details(request, fruit_id):
    profile = Profile.objects.all().first()
    fruit = Fruit.objects.filter(id=fruit_id).first()

    context = {
        "fruit": fruit,
        "profile": profile
    }

    return render(request, 'fruits/details-fruit.html', context)


def fruit_edit(request, fruit_id):
    profile = Profile.objects.all().first()
    fruit = Fruit.objects.filter(id=fruit_id).first()

    form = EditFruitModelForm(instance=fruit)

    if request.method == "POST":
        form = EditFruitModelForm(request.POST, instance=fruit)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        "form": form,
        "fruit": fruit,
        "profile": profile
    }

    return render(request, 'fruits/edit-fruit.html', context)


def fruit_delete(request, fruit_id):
    fruit = Fruit.objects.filter(id=fruit_id).first()
    form = DeleteFruitModelForm(instance=fruit)

    if request.method == "POST":
        form = DeleteFruitModelForm(request.POST, instance=fruit)
        if form.is_valid():
            fruit.delete()
            return redirect('dashboard page')

    context = {
        "form": form,
        "fruit": fruit
    }

    return render(request, 'fruits/delete-fruit.html', context)


def profile_create_page(request):
    form = ProfileCreateModelForm()
    profile = Profile.objects.all().first()

    if request.method == "POST":
        form = ProfileCreateModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard page')

    context = {
        "form": form,
    }

    return render(request, 'profiles/create-profile.html', context)


def profile_details_page(request):
    profile = Profile.objects.all().first()
    fruits = Fruit.objects.all()
    fruits_count = len(fruits)

    context = {
        "profile": profile,
        "fruits_count": fruits_count
    }
    return render(request, 'profiles/details-profile.html', context)


def profile_edit_page(request):
    profile = Profile.objects.all().first()
    form = ProfileEditModelForm(instance=profile)

    if request.method == "POST":
        form = ProfileEditModelForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')

    context = {
        "form": form,
        "profile": profile
    }

    return render(request, 'profiles/edit-profile.html', context)


def profile_delete_page(request):
    profile = Profile.objects.all().first()
    fruits = list(Fruit.objects.all())

    if request.method == "POST":
        profile.delete()
        # for fruit in fruits:
        #     fruit.delete()
        return redirect('index page')

    context = {
        "profile": profile
    }

    return render(request, 'profiles/delete-profile.html', context)
