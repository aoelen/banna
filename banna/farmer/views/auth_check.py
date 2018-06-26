
def is_farmer(user):
    return user.groups.filter(name='farmer').exists()
