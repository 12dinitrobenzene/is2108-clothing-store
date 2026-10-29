from django.core.exceptions import PermissionDenied

from .models import VendorEmployee
from .roles import VENDOR_EMPLOYEE_GROUP, role_for_user


def get_employee_for_user(user):
    if (
        not user.is_authenticated
        or not user.is_active
        or role_for_user(user) != VENDOR_EMPLOYEE_GROUP
    ):
        raise PermissionDenied("Vendor employee access is required.")

    try:
        return VendorEmployee.objects.select_related("vendor").get(
            user=user
        )
    except VendorEmployee.DoesNotExist:
        raise PermissionDenied(
            "Your account is not linked to a vendor."
        )
