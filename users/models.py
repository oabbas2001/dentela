from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager




#user modification
class CustomAccountManager(BaseUserManager):
    def create(self, email, full_name, password, **other_fields):
        print(other_fields)
        if not email:
            raise ValueError("you must provide an email address")
        email = self.normalize_email(email)
        
        user = self.model(email=email, full_name=full_name, **other_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, full_name, password, **other_fields):
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('verified', True)
        other_fields.setdefault('banned', False)
        other_fields.setdefault('is_superuser', True)

        return self.create(email, full_name, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField(max_length=100, )
    age = models.IntegerField(default=10)
    sex = models.CharField(max_length=6, choices=(
        ('male', 'male'), ('female', 'female')))
    phone_number = models.IntegerField(default=10)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    verified = models.BooleanField(default=False)
    banned = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True,)
    
    is_active = models.BooleanField(default=True)
    id_photo = models.ImageField ( upload_to='media/id/%y/%m/%d/' ,default= "media/id/meow_lostcat (1).png")
    profile_photo = models.ImageField ( upload_to=f'media/profiles_photo/%y/%m/%d/%h' ,default= "media/profiles_photo/meow_lostcat (1).png")
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['full_name', 'password']
    objects = CustomAccountManager()
    def __str__(self):
        return self.full_name

#student table
class Student (models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE,primary_key=True)
    university = models.CharField(max_length=100)
    year = models.IntegerField()
    patient_type_required = models.CharField(max_length=100)
    university_id_photo = models.ImageField ( upload_to='media/university_id/%y/%m/%d' )

#doctor table
class Doctors (models.Model):
     user = models.OneToOneField(User,on_delete= models.CASCADE,primary_key=True)
     clinic_address = models.CharField(max_length=200)
     doctor_specilization = models.CharField(max_length=100)
     certificate_photo = models.ImageField ( upload_to='media/certificate/%y/%m/%d' )
     rate = models.IntegerField()
     work_hours = models.IntegerField()
#PATIENT TABLE
class Patient(models.Model):
    user = models.OneToOneField(User,on_delete= models.CASCADE,primary_key=True)
    chronic_diseases = models.CharField(max_length=200)
    medicines = models.CharField(max_length=200)
    allergics = models.CharField(max_length=200)

#FOLLOWER TABLE
class UserFollowing(models.Model):
    user = models.ForeignKey(User,related_name='following',on_delete= models.CASCADE)
    following_user = models.ForeignKey(User,related_name='follower',on_delete= models.CASCADE)

    class Meta:
        unique_together =('user','following_user')

    