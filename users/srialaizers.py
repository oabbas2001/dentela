from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import User ,Doctors,Patient,Student,CustomAccountManager , UserFollowing


class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = get_user_model()
        fields = "__all__"

class TokenObtainPairSerializerNew(TokenObtainPairSerializer):
    def validate(self,attrs):
        Token=super().validate(attrs)
        Token['type']=self.user.groups.first().name
        return Token



#doctor register
class DOctorSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=100,source ="user.full_name" )
    age = serializers.IntegerField(default=10,source ="user.age")
    sex = serializers.CharField(max_length=6, source ="user.sex")
    phone_number = serializers.IntegerField(default=10,source ="user.phone_number")
    email = serializers.EmailField(source ="user.email")
    password = serializers.CharField(style ={"input_type":"password"},write_only=True)
    id_photo = serializers.ImageField (source ="user.id_photo")
    profile_photo = serializers.ImageField ( source ="user.profile_photo")
    
    class Meta :
        model = Doctors
        fields = ['full_name','age','sex','phone_number','email','password',
                  'id_photo','profile_photo','clinic_address','doctor_specilization',
                  'certificate_photo','rate','work_hours']
    
    
    def create(self, validated_data):
        
        email =validated_data['user'].pop('email')
        full_name = validated_data['user'].pop('full_name')
        password =validated_data.pop('password')
        dict={#'email':validated_data['User'].pop('email'),
             #'full_name':validated_data['User'].pop('full_name') ,
             #'password':validated_data['User'].pop('password'),
             'age':validated_data['user'].pop('age'),
             'sex':validated_data['user'].pop('sex'),
              'phone_number':validated_data['user'].pop('phone_number'),
              'id_photo':validated_data['user'].pop('id_photo'),
              'profile_photo':validated_data['user'].pop('profile_photo')}
       

        new_user=User.objects.create(email,full_name,
                                     password,**dict)
        
        new_user.groups.set([1])
        validated_data['user']=new_user
        
        return super().create(validated_data)



#student register
class Studentserializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=100,source ="user.full_name" )
    age = serializers.IntegerField(default=10,source ="user.age")
    sex = serializers.CharField(max_length=6, source ="user.sex")
    phone_number = serializers.IntegerField(default=10,source ="user.phone_number")
    email = serializers.EmailField(source ="user.email")
    password = serializers.CharField(style ={"input_type":"password"},write_only=True)
    id_photo = serializers.ImageField (source ="user.id_photo")
    profile_photo = serializers.ImageField ( source ="user.profile_photo")

    class Meta :
        model = Student
        fields = ['full_name','age','sex','phone_number','email','password',
                  'id_photo','profile_photo','university','year',
                  'patient_type_required','university_id_photo']

    def create(self, validated_data):
        email =validated_data['user'].pop('email')
        full_name = validated_data['user'].pop('full_name')
        password =validated_data.pop('password')
        dict={#'email':validated_data['User'].pop('email'),
             #'full_name':validated_data['User'].pop('full_name') ,
             #'password':validated_data['User'].pop('password'),
             'age':validated_data['user'].pop('age'),
             'sex':validated_data['user'].pop('sex'),
              'phone_number':validated_data['user'].pop('phone_number'),
              'id_photo':validated_data['user'].pop('id_photo'),
              'profile_photo':validated_data['user'].pop('profile_photo')}
        new_user=User.objects.create(email,full_name,
                                     password,**dict)
        new_user.groups.set([2])
        validated_data['user']=new_user
        
        return super().create(validated_data)
    

#patients 
class Patientserializer(serializers.ModelSerializer):
    full_name = serializers.CharField(max_length=100,source ="user.full_name" )
    age = serializers.IntegerField(default=10,source ="user.age")
    sex = serializers.CharField(max_length=6, source ="user.sex")
    phone_number = serializers.IntegerField(default=10,source ="user.phone_number")
    email = serializers.EmailField(source ="user.email")
    password = serializers.CharField(style ={"input_type":"password"},write_only=True)
    id_photo = serializers.ImageField (source ="user.id_photo")
    profile_photo = serializers.ImageField ( source ="user.profile_photo")
    
    class Meta :
        model = Patient
        fields = ['full_name','age','sex','phone_number','email','password',
                  'id_photo','profile_photo','chronic_diseases','medicines',
                  'allergics']
    def create(self, validated_data):
        email =validated_data['user'].pop('email')
        full_name = validated_data['user'].pop('full_name')
        password =validated_data.pop('password')
        dict={#'email':validated_data['User'].pop('email'),
             #'full_name':validated_data['User'].pop('full_name') ,
             #'password':validated_data['User'].pop('password'),
             'age':validated_data['user'].pop('age'),
             'sex':validated_data['user'].pop('sex'),
              'phone_number':validated_data['user'].pop('phone_number'),
              'id_photo':validated_data['user'].pop('id_photo'),
              'profile_photo':validated_data['user'].pop('profile_photo')}
        new_user=User.objects.create(email,full_name,
                                     password,**dict)
        new_user.groups.set([2])
        validated_data['user']=new_user
        
        return super().create(validated_data)
        
    

#follow serializer
class USerFollowingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only =True)
    following_user =UserSerializer(read_only =True)

    class Meta:
        model =UserFollowing
        fields = ['user','following_user']

