from django import forms
from .models import Ann
from django.core.exceptions import ValidationError


class AnnForm(forms.ModelForm):

    class Meta:
        model = Ann
        fields = [
            'title',
            'text',
            'category',
            'upload'

        ]

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get("title")
        description = cleaned_data.get("text")

        if name == description:
            raise ValidationError(
                "Описание не должно быть идентично названию."
            )

        return cleaned_data

    def clean_title(self):
        name = self.cleaned_data["title"]
        if name[0].islower():
            raise ValidationError(
                "Название должно начинаться с заглавной буквы"
            )
        return name
