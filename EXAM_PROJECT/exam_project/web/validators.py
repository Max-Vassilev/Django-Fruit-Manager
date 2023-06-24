from django.core.exceptions import ValidationError


def alpha_first(value):
    first_sym = value[0]

    if not first_sym.isupper():
        raise ValidationError("Your name must start with a letter!")


def alpha_only(value):
    for sym in value:
        if not sym.isalpha():
            raise ValidationError("Fruit name should contain only letters!")
