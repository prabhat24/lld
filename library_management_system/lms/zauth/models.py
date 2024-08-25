from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import gettext_lazy as _
# Create your models here.
from phonenumber_field.modelfields import PhoneNumberField



class ZUserManager(UserManager):

    def create(self, **obj_data):
        if not obj_data.get('username'):
            raise ValueError("user must have username")
        if not obj_data.get('email'):
            raise ValueError("user must have email")
        if not obj_data.get('mobile_no'):
            raise ValueError("user must have mobile_no")
        return super().create(**obj_data)

class User(AbstractUser):
    """
    Users within the Django authentication system are represented by this
    model.

    Username and password are required. Other fields are optional.
    """
    username_validator = UnicodeUsernameValidator()
    username = models.CharField(
        _("username"),
        max_length=150,
        unique=True,
        null=False,
        blank=False,
        help_text=_(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    email = models.EmailField(_("email address"), null=False, blank=True)
    mobile_no = PhoneNumberField(blank=False, null=False)
    address = models.TextField("Email Body", blank=True)
    metadata = models.JSONField(null=True, blank=False)

    objects = ZUserManager()

class LibrarianManager(UserManager):

    def create_user(self, **obj_data):
        try:
            user = User.objects.create(**obj_data)
        except Exception as e:
            raise e
        return super().create(user=user)

class MemberManager(UserManager):

    def create_user(self, **obj_data):
        try:
            user = User.objects.create(**obj_data)
        except Exception as e:
            raise e
        return super().create(user=user)

class Librarian(models.Model):
    user = models.OneToOneField(User, 
            null=False,
            on_delete=models.CASCADE,
            related_name='librarian')
    
    objects = LibrarianManager()

class Member(models.Model):
    user = models.OneToOneField(User, 
            null=False,
            on_delete=models.CASCADE,
            related_name='member')

    objects = MemberManager()


# admin registration
admin.site.register(Librarian)
admin.site.register(Member)
admin.site.register(User)