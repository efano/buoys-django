from django import forms
from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.
class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=12, required=True)
    last_name = forms.CharField(max_length=12, required=True)
    agency = forms.CharField(max_length=100, required=True)

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2',
                  'email', 'first_name', 'last_name', 'agency')

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.agency = self.cleaned_data['agency']

        if commit:
            user.save()
        return user


class NewCommentForm(forms.Form):
    body = forms.CharField(max_length=255, label=False, widget=forms.TextInput(
        attrs={'class': "form-control form-control-sm comments-input pe-4 me-5",
               'placeholder': "add comment",
               'aria-label': "add comment",
               'aria-describedby': "button-addon2"
               }))
