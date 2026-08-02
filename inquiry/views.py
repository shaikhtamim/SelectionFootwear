from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact(request):

    print("REQUEST METHOD:", request.method)

    if request.method == "POST":

        print("POST DATA:", request.POST)

        form = ContactForm(request.POST)

        if form.is_valid():
            print("FORM IS VALID")

            form.save()

            messages.success(request, "Your message has been sent successfully!")

            return redirect("contact")

        else:
            print(form.errors)

    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})