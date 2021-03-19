from django.db import models
import jwt

from datetime import datetime
from datetime import timedelta

from django.conf import settings
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin

"""
§§ALL COMMENTARIES BY BEKET 18BD110390,
FOR REMEMBERING IT AND TO BE EASY WHEN IMPLEMENT IT TO OTHER PROJECTS
"""

class User(PermissionsMixin, AbstractBaseUser):
    """
    §§HERE WE DEFINE OUR CUSTOM USER CLASS
    THEIR USERNAME EMAIL AND PASSWORD WHICH ARE REQUIRED§§
    """

    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(validators=[validators.validate_email],
                              unique=True, blank=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    """
    §§USERNAME_FIELD WHICH FIELD IS USED TO LOG IN
    """
    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ('username',)

    """
    §§TELLS TO DJANGO THAT USERMANAGER CLASS DEFINED ABOVE SHOULD MANAGE,
    OBJECTS OF THIS TYPE
    """
    objects = UserManager()

    def __str__(self):
        """
        §§§Returns a string representation of this 'User'
        This string is when a 'User' is printed in the console
        """
        return self.username

    @property
    def token(self):
        """
        Позволяет нам получать токен юзера по USER.TOKEN, вместо USER.GENERATE_JWT_TOKEN()
        А вот @PROPERTY decorator vyshe delaet eto vozmozhnym.
        TOKEN vyzyvaetsya 'dynamic_property'
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Etot metod required by DJANGO dlya handlinga emailov.
        Obychno eto mog byt imya i familiya usera
        No tak kak my ne sohranyaem ih imena, my vozvrawaem username
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Generiruet JWT TOKEN kotory sohranyaet etot USER'S ID and
        expiretsya za 60 day v buduwem
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

"""
TOKEN sozdalsya dinamicheski s @property. UserManager kotory vyzyvetsya kogda sozdatsya 
new user vnizu
"""
from django.contrib.auth.models import BaseUserManager
class UserManager(BaseUserManager):
    """
    Django trebuet chtoby customny usera oboznachali svoego Manager classa
    S nasleduet ot BASEUSERMANAGER
    My poluchaem a odinakovy code kotory ispolzovalsya by Django,
    dlya sozdaniya Usera

    Vse chto my dolzhny sdelat eto override 'create_user", kotory
    sozdaet User objectov
    """
    def _create_user(self, username, email,
                     password=None, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        ###what is _db
        user.save(using=self._db)
