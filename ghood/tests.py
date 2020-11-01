from django.test import TestCase
from .models import Profile,Post,Business,Neighbourhood
from django.contrib.auth.models import User

class TestProfile(TestCase):
    def setUp(self):
        self.user = User(username = 'Charles',email= 'doryn@gmail.com', password = '3rt5')
        self.user.save()
        
        self.neighbourhood = Neighbourhood(name = 'Charles', description = 'Next to langata', police_number = 910, healthcenter_number = 56 )
        self.neighbourhood.save()
        
        self.profile = Profile(user=self.user, name='Osango', bio='my bio',profile_picture = 'image.png', location = 'raila', neighbourhood = self.neighbourhood)
        
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, Profile))
        
    def test_save_profile(self):
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles)>0)
        
    def test_delete_profile(self):
        profile = Profile.objects.all().delete()
        self.assertTrue(len(profile)>0)
        
    def tearDown(self):
        Profile.objects.all().delete()
        
