from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from .models import CustomUser,Cities,Semesters,Desposites,Profile

class UserSerializer(serializers.ModelSerializer):
   class Meta:
       model = CustomUser
       fields = ['username', 'email', 'password']
       extra_kwargs = {'password': {'write_only': True}}


   def create(self, validated_data):
       user = CustomUser(
           username=validated_data['username'],
           email=validated_data['email'],
       )
       user.set_password(validated_data['password'])
       user.save()
       return user

class CitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cities
        fields = ['city', 'city_person']

    def validate(self, data):
        unknown = set(data) - set(self.fields)
        if unknown:
            raise ValidationError(f"Unknown field(s): {', '.join(unknown)}")
        return data

class SemestersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semesters
        fields = ['semester', 'semester_person']

    def validate(self, data):
        unknown = set(data) - set(self.fields)
        if unknown:
            raise ValidationError(f"Unknown field(s): {', '.join(unknown)}")
        return data

class DespositesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Semesters
        fields = ['user', 'copy','issue_date','due_date']
    def validate(self, data):
        unknown = set(data) - set(self.fields)
        if unknown:
            raise ValidationError(f"Unknown field(s): {', '.join(unknown)}")
        return data


class DespositesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Desposites
        fields = ['user', 'copy','issue_date','due_date']

    def validate(self, data):
        unknown = set(data) - set(self.fields)
        if unknown:
            raise ValidationError(f"Unknown field(s): {', '.join(unknown)}")
        return data


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'first_name','last_name','father_name','contact_no','identification_no',
                  'registration_no','page_no','original_address','current_address','signature']

    def validate(self, data):
        unknown = set(data) - set(self.fields)
        if unknown:
            raise ValidationError(f"Unknown field(s): {', '.join(unknown)}")
        return data



