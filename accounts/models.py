from django.db import models
from accounts.managers import CustomUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
import uuid
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from accounts.model_functions import generate_token

GENDER_CHOICES = (
    ("male", "male"),
    ("female", "female"),
    
)

ACCOUNT_TOKEN_CHOICES = (
    ("activation", "activation"),
    ("recovery", "recovery"),
)


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    first_name = models.CharField(verbose_name=(_("First name")),max_length=300)
    last_name = models.CharField(verbose_name=(_("Last name")),max_length=300)
    email = models.EmailField(verbose_name=(_("Email address")), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    gender = models.CharField(choices= GENDER_CHOICES, max_length= 10, blank = True, null = True)
    address = models.CharField(blank = True, null = True, max_length= 100)
    vat_no = models.CharField(max_length=1000)
    hrb_no = models.CharField(max_length=1000,blank = True, null = True)
    company_reg_no = models.CharField(max_length=1000)
    tax_id_number = models.CharField(max_length=1000)
    identification = models.FileField(upload_to="identification/")
    dealer = models.BooleanField(default=False)
    seller = models.BooleanField(default=False)
    approved_seller = models.BooleanField(default=False)
    country = models.CharField(max_length=10, default = "GERMANY")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)


class AccountToken(models.Model):
    user = models.ForeignKey(User, on_delete =models.CASCADE)
    token = models.PositiveIntegerField(editable=False, default=generate_token, unique=True)
    creation_time = models.DateTimeField(auto_now_add=True)
    purpose = models.CharField(max_length=10, choices=ACCOUNT_TOKEN_CHOICES)