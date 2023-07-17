from django import forms
from home.models import Todo

class TodoCreateForm(forms.Form):
    title = forms.CharField(label='عنوان')
    body = forms.CharField(label='توضیحات')
    created = forms.DateTimeField(label='تاریخ و ساعت')


class TodoUpdateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ('title', 'body', 'created')
