from django.shortcuts import render
from django.db.models import Prefetch, Q
from django.shortcuts import get_object_or_404, render

from .models import Category, Product, ProductVariant, Vendor

## Landing page view
def landing(request):
    return render(request, "shop/public/landing.html")


def catalogue(request):
    products = visible_products()
    categories = Category.objects.filter(
        products__in=products
    ).distinct()

    selected_category = request.GET.get("category", "")
    query = request.GET.get("q", "").strip()
    invalid_category = False

    # Keep your existing category filter.
    if selected_category:
        if selected_category.isdigit() and categories.filter(
            pk=selected_category
        ).exists():
            products = products.filter(category_id=selected_category)
        else:
            products = products.none()
            invalid_category = True

    # Search within the permitted, category-filtered products.
    if query:
        products = products.filter(
            Q(name__icontains=query)
            | Q(description__icontains=query)
        )

    return render(
        request,
        "shop/customer/catalogue.html",
        {
            "products": products,
            "categories": categories,
            "selected_category": selected_category,
            "invalid_category": invalid_category,
            "query": query,
        },
    )



def style_preferences(request):
    return render(
        request,
        "shop/public/section_placeholder.html",
        {
            "title": "Style preferences",
            "message": "Personal style preferences will be available here.",
        },
    )

def customer_home(request):
    # Temporary selection until ML workflow is done ok - ck
    available_products = visible_products().order_by("-pk")
    products = available_products[:8]
    featured_vendors = Vendor.objects.filter(
        products__in=available_products,
    ).order_by("name").distinct()[:4]

    return render(
        request,
        "shop/customer/customer_home.html",
        {
            "products": products,
            "featured_vendors": featured_vendors,
        },
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
