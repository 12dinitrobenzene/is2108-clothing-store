from .roles import role_for_user


def account_navigation(request):
    return {
        "account_role": role_for_user(request.user),
    }
