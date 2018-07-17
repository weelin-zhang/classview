from django import forms

from .models import Post

class PostModelForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Post
        fields = ("title", "body")
        widgets = {
            "body": forms.TextInput
        }