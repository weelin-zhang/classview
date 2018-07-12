from django import forms
from .models import Book, Author
class AuthorForm(forms.Form):
    # 既可以在__init__中定制表单控件，也可在在声明属性时自定义
    
    # name = forms.CharField(required=True, max_length=10, widget=forms.TextInput,
    #                        error_messages={"required": "请正确输入作者名字输入", "max_length": "最多20个字符"})
    
    # 声明属性时自定义
    name = forms.CharField(label="作者", required=True, max_length=10, widget=forms.TextInput(attrs={"class":
                                                                                                     "form-control",
                                                                                       "placeholder": "fdk"},),
                           error_messages={"required": "请正确输入作者名字输入", "max_length": "最多20个字符"})
    
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        # 在init过程中自定义
        # for name, field in self.fields.items():
        #     # print(name, field, field.label)
        #     field.widget.attrs['placeholder'] = "20个字符以内"
        # self.fields['name'].widget.attrs['class'] = "form-control"
        


class BookCreateForm(forms.ModelForm):
   
    choices = [(author, author.name) for author in Author.objects.all()]
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            
    class Meta:
        model = Book
        fields = ['name', 'price', 'author']
        # widgets = {
        #     'name': forms.PasswordInput
        # }
        # exclude = []



class BookUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
    
    class Meta:
        model = Book
        fields = ['price', 'author']
        # widgets = {
        #     'name': forms.PasswordInput
        # }
        # exclude = []
