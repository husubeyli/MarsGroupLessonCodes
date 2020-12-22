
def update_user_social_data(strategy, *args, **kwargs):
    response = kwargs['response']
    print(response)
    backend = kwargs['backend']
    user = kwargs['user']
    user_id = response.get('id')
    if user.image:
        return None
    picture = response.get('picture')
    if isinstance(picture, dict):
        picture_data = f'http://graph.facebook.com/{user_id}/picture?width=600&height=600'
        user.image = picture_data
    else:
        user.image = picture
    user.save()
