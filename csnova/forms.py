from django import forms


class PersonInfo(forms.Form):
    nickname = forms.CharField(label="姓名", max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label="实验室", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="方向", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="邮箱地址", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    intro = forms.CharField(label="方向", max_length=256, widget=forms.TextInput(attrs={'class': 'form-control'}))
    
    