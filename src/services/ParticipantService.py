from team.models import Participation

# participant spausdint roliu /kita info
# Identity role participant
# Tik adminui enra apribojimu kai bookina
# Admin/Assistant kai bukina nurodo kita user id kiti to negali


def identity_roles(user):
    print("Identity roles")
    # users = Participation.objects.all()
    # for user in users:
    #     # print(i.id, i.team, i.account, i.role)

    for a in Participation.ROLE:
        if user.role == a[0]:
            return user.role, a[1]
