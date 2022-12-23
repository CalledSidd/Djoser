from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class AccountManager(BaseUserManager):
    pass

class UserAccount(AbstractBaseUser, PermissionsMixin):
    STATES = (
        ('Arunachal Pradesh', 'Arunachal Pradesh'),
        ('Assam','Assam'),
        ('Bihar','Bihar'),
        ('Chhattisgarh','Chhattisgarh'),
        ('Goa','Goa'),
        ('Gujarat','Gujarat'),
        ('Haryana','Haryana'),
        ('Himachal Pradesh','Himachal Pradesh'),
        ('Jammu and Kashmir','Jammu and Kashmir'),
        ('Jharkhand','Jharkhand'),
        ('Karnataka','Karnataka'),
        ('Kerala','Kerala'),
        ('Madhya Pradesh','Madhya Pradesh'),
        ('Maharashtra','Maharashtra'),
        ('Manipur','Manipur'),
        ('Meghalaya','Meghalaya'),
        ('Mizoram','Mizoram'),
        ('Nagaland','Nagaland'),
        ('Odisha','Odisha'),
        ('Punjab','Punjab'),
        ('Rajasthan','Rajasthan'),
        ('Sikkim','Sikkim'),
        ('Tamil Nadu','Tamil Nadu'),
        ('Telangana','Telangana'),
        ('Tripura','Tripura'),
        ('Uttar Pradesh','Uttar Pradesh'),
        ('Uttarakhand','Uttarakhand'),
        ('West Bengal','West Bengal'),
        ('Puducherry','Puducherry'),
        ('Lakshadweep','Lakshadweep'),
        ('Ladakh ','Ladakh '),
        ('Delhi','Delhi'),
        ('Daman and Diu','Daman and Diu'),
        ('Chandigarh','Chandigarh'),
        ('Andaman and Nicobar Islands','Andaman and Nicobar Islands'),
    )
    email        = models.EmailField(max_length=255, unique=True)
    name         = models.CharField(max_length=255)
    username     = models.CharField(max_length=255, unique=True)
    phone        = models.CharField(max_length=10, unique=True)
    state        = models.CharField(max_length=30, choices=STATES, null=True, blank=True)
    # permissions and stuff
    is_active    = models.BooleanField(default=True)
    is_staff     = models.BooleanField(default=False)
    is_admin     = models.BooleanField(default=False)
    is_superadmin = models.BooleanField(default=False)
    joining_date = models.DateTimeField(auto_now_add=True)
    objects = AccountManager()
    def __str__(self):
        return self.name