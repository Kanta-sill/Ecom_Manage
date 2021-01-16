from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['name', 'item_price', 'item_desc', 'item_image']