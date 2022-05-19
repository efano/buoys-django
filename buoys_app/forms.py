from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'email')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

# class NewSignupForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=20)
#     password = forms.CharField(
#         widget=forms.PasswordInput, label='Password', max_length=10)
#     first_name = forms.CharField(label='First Name', max_length=20)
#     last_name = forms.CharField(label='LastName', max_length=20)
#     email = forms.EmailField(label='Email')


# class NewLoginForm(forms.Form):
#     username = forms.CharField(label='Username', max_length=20)
#     password = forms.CharField(
#         widget=forms.PasswordInput, label='Password', max_length=10)
