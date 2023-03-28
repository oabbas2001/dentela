from .srialaizers import UserSerializer
from django.contrib.auth import get_user_model
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets , generics
from rest_framework.authentication import SessionAuthentication, BaseAuthentication, TokenAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView
from .srialaizers import TokenObtainPairSerializerNew ,DOctorSerializer,Studentserializer,Patientserializer
from .models import User ,Doctors,Patient,Student,CustomAccountManager ,UserFollowing



class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = get_user_model().objects.all()
    permission_classes = [IsAuthenticated,]


class TokenObtainPairViewNew(TokenObtainPairView):
    serializer_class=TokenObtainPairSerializerNew
token_obtain_pair = TokenObtainPairViewNew.as_view()

class creat_doctorview(generics.CreateAPIView):
    serializer_class = DOctorSerializer
    queryset=Doctors.objects.all()
    

create_doctor_view = creat_doctorview.as_view()


class Creat_studentview(generics.CreateAPIView):
    serializer_class = Studentserializer
    queryset=Student.objects.all()

class Creat_patientview(generics.CreateAPIView):
    serializer_class = Patientserializer
    queryset=Patient.objects.all()


