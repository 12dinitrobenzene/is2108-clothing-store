from django.shortcuts import render
from django.db.models import Prefetch
from django.shortcuts import get_object_or_404, render

from .models import Product, ProductVariant, Vendor

## Landing page view
def landing(request):
    return render(request, "shop/public/landing.html")



## Product Views for the customer-facing catalogue and product detail pages
def catalogue(request):
    products = visible_products()

    return render(
        request,
        "shop/customer/catalogue.html",
        {"products": products},
    )

def product_detail(request, product_id):
    product = get_object_or_404(
        visible_products(),
        pk=product_id,
    )

    related_products = (
        visible_products()
        .filter(category=product.category)
        .exclude(pk=product.pk)[:4]
    )

    total_stock = sum(
        variant.total_quantity
        for variant in product.active_variants
    )

    available_colours = []
    seen_colours = set()

    for variant in product.active_variants:
        colour_key = variant.colour.strip().casefold()

        if colour_key not in seen_colours:
            seen_colours.add(colour_key)
            available_colours.append(
                {
                    "name": variant.colour,
                    "hex": variant.colour_hex,
                }
            )

    default_colour = (
        available_colours[0]["name"]
        if available_colours
        else ""
    )

    return render(
        request,
        "shop/customer/product_detail.html",
        {
            "product": product,
            "related_products": related_products,
            "total_stock": total_stock,
            "available_colours": available_colours,
            "default_colour": default_colour,
        },
    )


## Employee and Platform Admin Views for the internal dashboard
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

def visible_products():
    return (
        Product.objects.filter(
            vendor__approval_status=Vendor.ApprovalStatus.APPROVED,
            vendor__is_suspended=False,
            is_archived=False,
            moderation_blocked=False,
            variants__is_active=True,
        )
        .select_related("vendor", "category")
        .prefetch_related(
            "images",
            Prefetch(
                "variants",
                queryset=ProductVariant.objects.filter(
                    is_active=True,
                    total_quantity__gt=0,
                ),
                to_attr="active_variants",
            ),
        )
        .distinct()
    )
