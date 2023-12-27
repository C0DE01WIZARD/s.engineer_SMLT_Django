from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин",
                               widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label="Логин",
                               widget=forms.PasswordInput(attrs={'class': 'form-input'}))
