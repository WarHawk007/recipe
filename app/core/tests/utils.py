from django.contrib.auth import get_user_model


def create_test_superuser(email, password):
    return get_user_model().objects.create_superuser(
        email, password
    )


def create_test_user(email, password, **kwargs):
    return get_user_model().objects.create_user(
        email, password, **kwargs
    )
