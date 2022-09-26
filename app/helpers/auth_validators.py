"""users package custom form validators"""
from flask_login import current_user
from wtforms import ValidationError
from models.account import Account


def unique_or_current_user_field(message=None):
    """Validates that email field is either equal to the user's current field
    or doesn't exist in the database
    """

    def validation(form, field):
        kwargs = {field.name: field.data}
        if (
                hasattr(current_user, field.name)
                and getattr(current_user, field.name) == field.data
        ):
            return
        if Account.objects(**kwargs).first():
            raise ValidationError(message)

    return validation
