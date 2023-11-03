from .models import Comment,Accounts
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name','email','body')
        
        
class AccountsForm(forms.ModelForm):
    class Meta:
        model = Accounts
        fields = ('name','email','username','password')