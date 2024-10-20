from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from allauth.account.forms import SignupForm


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "email", "age", "address", "phone_number")


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ("username", "first_name", "last_name", "email", "age", "address", "phone_number")


class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=30, label="First Name")
    last_name = forms.CharField(max_length=30, label="Last Name")
    age = forms.IntegerField(label="Age")
    phone_number = forms.CharField(max_length=15, label="Phone number")
    address = forms.CharField(max_length=700, label="Address")

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.age = self.cleaned_data["age"]
        user.phone_number = self.cleaned_data["phone_number"]
        user.address = self.cleaned_data["address"]

        user.save()
        return user

