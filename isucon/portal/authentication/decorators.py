from django.contrib.auth.decorators import user_passes_test

def has_team(user):
    return user.is_authenticated and user.team is not None

team_is_authenticated = user_passes_test(has_team)

def is_staff(user):
    return user.is_authenticated and user.is_staff

admin_is_authenticated = user_passes_test(is_staff)
