from django import forms
from .models import User, Post

query = User.objects.values_list('username')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','email','password','username']



class PostForm(forms.Form):
    user = forms.ModelChoiceField(queryset=query)
    text = forms.CharField( widget=forms.Textarea )
