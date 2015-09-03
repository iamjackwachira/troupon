from django.contrib.auth.forms import UserCreationForm
from account.models import Account 
from django import forms


class MySignupForm(UserCreationForm):
    email = forms.EmailField(required = True)
    first_name = forms.CharField(required = True)
    last_name = forms.CharField(required=True)
    username = forms.CharField(required = True)


    class meta:
        model = Account
        fields = ('id','email', 'username', 'created_at', 'updated_at',
                  'first_name', 'last_name', 'password1','password2',)

        created_at = forms.DateTimeField(widget=forms.TextInput(attrs={'readonly':'readonly'}))

        updated_at = forms.DateTimeField(widget=forms.TextInput(attrs={'readonly':'readonly'}))


        def save(self, commit=True):          
          user = super(MySignupForm, self).save(commit=False)
          user.email = self.cleaned_data['email']
          user.first_name = self.cleaned_data['first_name']
          user.last_name = self.cleaned_data['last_name']
          user.username = self.cleaned_data['username']
          user.is_staff = True

          if commit:
            user.save()
          return user

