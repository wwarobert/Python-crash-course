def build_profile(first, last, **user_info):
    """Build a dictionary containning everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile(
    'albert', 'einstein', location='princeton', field='physics')
print(user_profile)

user_profile = build_profile(
    'Dennis', 'Coles', profession='Python Developer', location='Netherlands', city='Den Haag')
print(user_profile)
