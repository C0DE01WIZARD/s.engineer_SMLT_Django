from django import forms


class LoginUserForm(forms.Form):
    username = forms.CharField(label="Логин  :",widget=forms.TextInput(attrs={'class': 'formauth'}))
    password = forms.CharField(label="Пароль",widget=forms.PasswordInput(attrs={'class': 'formauth'}))
