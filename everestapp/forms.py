from .models import *
from django import forms
from django_summernote.widgets import SummernoteWidget

class ClientNewsCreateForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        widgets={
            'title':forms.TextInput(attrs={
                'class':'form-control',

            }),
            'category':forms.Select(),
            #'contebt':form.Textarea(attrs={
            #   'class':'form-control.summernote',}),
            'content': SummernoteWidget(attrs={
                'summernote': {
                    'class':'form_control form-control-rounded',
                    'placeholder': 'Page Description',
                    
                }
            }),
            'image': forms.ClearableFileInput(),
        }

class AdminLoginForm(forms.Form):
    usrname=forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': "username...",

    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': "Enter your password..."
    }))

    