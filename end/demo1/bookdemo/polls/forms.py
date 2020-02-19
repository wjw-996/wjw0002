from django import forms


class LonginForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2, label="输入用户名", help_text="最大20位，最小6位")
    password = forms.CharField(max_length=20, min_length=6, label="输入密码", widget=forms.PasswordInput,
                               help_text="最大20位，最小6位")