from django import forms
from .models import User, Services

class Sign_up(forms.ModelForm):
    confirm_password = forms.CharField(
        max_length=20,
        widget=forms.PasswordInput,
        label="Confirm Password"
    )

    class Meta:
        model = User
        fields = [
            'first_name', 'last_name', 'email', 
            'phone', 'address', 'username', 'password'
        ]
        widgets = {
            'password': forms.PasswordInput,  
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            self.add_error('confirm_password', "Passwords do not match.")
        return cleaned_data

class Login(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=20)
    
class Service_Requests(forms.ModelForm):
    class Meta:
        model = Services
        fields = ["file","service_type","description"]
        
    