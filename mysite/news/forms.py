from django import forms
from .models import *


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label="Название",
                            widget=forms.TimeInput(attrs={"class": "form-control"}))
    content = forms.CharField(label="Текст", required=False,
                              widget=forms.Textarea(attrs={"class": "form-control", "rows": 5}))
    is_published = forms.BooleanField(label="Опубликовано?", initial=True)
    category = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категория",
                                      empty_label="Выберите категорию",
                                      widget=forms.Select(attrs={"class": "form-control"}))
