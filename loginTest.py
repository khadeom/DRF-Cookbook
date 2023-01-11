from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

user = User.objects.get(pk=1)


print(Token.objects.create(user=user))

#e4a060449426f3bce0e2cbf705c6d36b35c5d63f > id 1 > can be generated only once

# Authorization: Token e4a060449426f3bce0e2cbf705c6d36b35c5d63f,


"e2d14cf13adc39e8bf5d95dad8204356e3364ea5"