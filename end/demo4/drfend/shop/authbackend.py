from django.contrib.auth import backends
from .models import User
from django.db.models import Q


class MyLoginBackend(backends.BaseBackend):
    def authenticate(self, request, **kwargs):
        username = kwargs["username"]
        password = kwargs["password"]

        user = User.objects.filter(Q(username=username) | Q(email=username) | Q(telephone=username)).first()
        print("1111111")
        if user:
            print("-------")
            b = user.check_password(password)
            if b:
                print("++++++++")
                return user
            else:
                None
        else:
            return None

