from team.models import Participation


def identity_roles(user):
    for role in Participation.ROLE:
        if user.role == role[0]:
            return user.role, role[1]


def identity_account(user):
    account_id = 0
    if user.username == "admin":
        account_id = 1
    elif user.username == "asistant":
        account_id = 2
    elif user.username == "user":
        account_id = 3

    return account_id