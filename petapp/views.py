from django.shortcuts import render, redirect
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.

def pet_list(request):
    context = {
        "pets": Pet.objects.filter(available=True),
    }
    return render(request, "pet_list.html", context)


def pet_detail(request, pet_id):
    pet_obj = Pet.objects.get(id=pet_id)

    context = {
    "pet": pet_obj,
    }

    return render(request, "pet_detail.html", context)

def pet_create(request):
    form = PetForm()
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.available = True
            pet.save()
            messages.success(request, "Successfully Created!")
            return redirect('pet-detail', pet.id)
    context = {
        "form":form,
    }
    return render(request, 'create.html', context)

def pet_update(request, pet_id):
    pet_obj = Pet.objects.get(id=pet_id)
    form = PetForm(instance=pet_obj)
    if request.method == "POST":
        form = PetForm(request.POST, request.FILES, instance=pet_obj)
        if form.is_valid():
            form.save()
            messages.success(request, "Successfully Updated!")
            return redirect('pet-detail', pet_obj.id)
    context = {
        "pet": pet_obj,
        "form":form,
    }
    return render(request, 'update.html', context)

def pet_delete(request, pet_id):
    Pet.objects.get(id=pet_id).delete()
    messages.success(request, "Successfully Deleted!")
    return redirect('pet-list')