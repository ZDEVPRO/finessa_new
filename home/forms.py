from django.forms import ModelForm, TextInput, Textarea
from contact.models import Aloqa


class AloqaForm(ModelForm):
    class Meta:
        model = Aloqa
        fields = ['first_name', 'last_name', 'product_id', 'phone', 'message']
        widgets = {
            'first_name': TextInput(attrs={'class': 'contact__form--input', 'placeholder': 'Ismingizni kiriting'}),
            'last_name': TextInput(attrs={'class': 'contact__form--input', 'placeholder': 'Familyangizni kiriting'}),
            'phone': TextInput(attrs={'class': 'contact__form--input', 'placeholder': 'Telefon raqamingizni kiriting'}),
            'message': Textarea(
                attrs={'class': 'contact__form--textarea', 'placeholder': 'Manzil va qo`shimcha xabarni kiriting...'}),
        }
