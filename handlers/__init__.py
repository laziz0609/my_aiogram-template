from . import admins, users, groups, chenels

# ❗ Tartib bo‘yicha: admin birinchi, user keyin
routers = [
    *admins.routers,
    *users.routers,
    *groups.routers,
    *chenels.routers,
]
