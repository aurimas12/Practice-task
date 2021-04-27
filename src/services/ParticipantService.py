from team.models import Participation

# participant spausdint roliu /kita info
# Identity role participant
# Tik adminui enra apribojimu kai bookina
# Admin/Assistant kai bukina nurodo kita user id kiti to negali


def identity_roles(user):
    for role in Participation.ROLE:
        if user.role == role[0]:
            return user.role, role[1]
