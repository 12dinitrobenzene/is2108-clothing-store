from django.shortcuts import render


def landing(request):
    return render(request, "shop/public/landing.html")


def catalogue(request):
    return render(request, "shop/customer/catalogue.html", {"products": []})


def employee_home(request):
    return render(
        request,
        "shop/public/section_placeholder.html",
        {
            "title": "Vendor employee",
            "message": "The employee workspace will be available here.",
        },
    )


def platform_admin_home(request):
    return render(
        request,
        "shop/public/section_placeholder.html",
        {
            "title": "Platform admin",
            "message": "The platform dashboard will be available here.",
        },
    )
