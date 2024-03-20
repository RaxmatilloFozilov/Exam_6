from django import forms
from .models import Item, Topic


class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'description']


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['description']
