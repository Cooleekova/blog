import pint
from pint.errors import UndefinedUnitError
from django.core.exceptions import ValidationError

valid_unit_measurements = ['pounds', 'lbs', 'oz', 'gram', ]


def validate_unit_of_measure(value):
    ureg = pint.UnitRegistry()
    try:
        single_unit = ureg[value]
    except UndefinedUnitError as e:
        raise ValidationError(f'{value} is not a valid unit of measure')
    except:
        raise ValidationError(f'{value} is invalid. Unknown error.')


