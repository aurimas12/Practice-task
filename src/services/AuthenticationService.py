from django.contrib.auth.models import User


def get_auth_user_name(request):
    user = User.objects.get(id=request.user.id)
    if user.is_authenticated:
        return user
