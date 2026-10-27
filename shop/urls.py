"""URL patterns for the shop application."""

from django.urls import path

from . import views

app_name = "shop"

urlpatterns = [
    path("", views.landing, name="landing"),
    path("customer/", views.customer_home, name="catalogue"),
    path("customer/catalogue/", views.catalogue, name="full_catalogue"),
    path("employee/", views.employee_home, name="employee_home"),
    path("platform-admin/", views.platform_admin_home, name="platform_admin_home"),
    path(
        "customer/products/<int:product_id>/",
        views.product_detail,
        name="product_detail",
    ),
    path(
        "customer/preferences/",
        views.style_preferences,
        name="style_preferences",
    ),
]
