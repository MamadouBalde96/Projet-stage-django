from django.forms import ModelForm
from.models import Listes

class ListesForm(ModelForm):
    class Meta: 
        model = Listes
        fields = ['nom', 'prénom', 'email', 'telephone', 'statut', 'niveau','UFR', 'département', 'parcours', 'groupe_de_TD', 'testPCR', 'sujet', 'message']