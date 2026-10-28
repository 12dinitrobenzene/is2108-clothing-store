from django.contrib import messages
from django.contrib.auth.models import Group
from django.db import transaction
from django.shortcuts import redirect, render

from .forms import CustomerRegistrationForm
from .models import CustomerProfile
from .roles import CUSTOMER_GROUP


def register(request):
    if request.user.is_authenticated:
        return redirect("shop:catalogue")

    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)

        if form.is_valid():
            with transaction.atomic():
                user = form.save()
                customer_group = Group.objects.get(name=CUSTOMER_GROUP)
                user.groups.add(customer_group)
                CustomerProfile.objects.create(user=user)

            messages.success(
                request,
                "Your customer account has been created. Sign-in will be available soon.",
            )
            return redirect("shop:landing")
    else:
        form = CustomerRegistrationForm()

    return render(request, "accounts/register.html", {"form": form})
