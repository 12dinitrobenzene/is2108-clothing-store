CUSTOMER_GROUP = "Customer"
VENDOR_EMPLOYEE_GROUP = "Vendor Employee"
PLATFORM_ADMIN_GROUP = "Platform Admin"

APPLICATION_ROLE_GROUPS = (
    CUSTOMER_GROUP,
    VENDOR_EMPLOYEE_GROUP,
    PLATFORM_ADMIN_GROUP,
)


ROLE_DESTINATIONS = {
    CUSTOMER_GROUP: "shop:catalogue",
    VENDOR_EMPLOYEE_GROUP: "shop:employee_home",
    PLATFORM_ADMIN_GROUP: "shop:platform_admin_home",
}


def destination_for_user(user):
    role_names = set(
        user.groups.filter(name__in=APPLICATION_ROLE_GROUPS).values_list(
            "name",
            flat=True,
        )
    )

    if len(role_names) != 1:
        return None

    return ROLE_DESTINATIONS[role_names.pop()]


def user_has_role(user, role_name):
    return user.is_authenticated and user.groups.filter(name=role_name).exists()
