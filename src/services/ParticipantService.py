from team.models import Participation


def identity_roles(user):
    for role in Participation.ROLE:
        if user.role == role[0]:
            return user.role, role[1]
