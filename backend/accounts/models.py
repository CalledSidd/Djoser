from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.
class AccountManager(BaseUserManager):
    # create normal user with the params
    def create_user(self, username, email, name, password=None):
        if not username:
            raise ValueError("User must have a username")
        if not email:
            raise ValueError("User must have an email")

        email = self.normalize_email(email)
        user = self.model(email=email, name = name, username = username)
        user.set_password(password)
        user.save(using = self._db)
        return user
    # creating superuser/admin
    def create_superuser(self, email, username, name, password):
        user = self.create_user(username, email, name, password)
        user.is_superuser = True
        user.is_staff     = True
        user.is_admin     = True
        user.save(using = self._db)
        return user 

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
    is_superuser = models.BooleanField(default=False)
    joining_date = models.DateTimeField(auto_now_add=True)


    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','phone']

    def get_name(self):
        return self.name

    def __str__(self):
        return self.username