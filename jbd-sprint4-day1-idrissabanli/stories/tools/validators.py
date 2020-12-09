from django.core.exceptions import ValidationError


def validate_email(email_data):
    if not email_data.endswith('@gmail.com'):
        raise ValidationError('Email must be gmail')
    return email_data