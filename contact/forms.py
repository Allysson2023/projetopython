from django import forms
from django.core.exceptions import ValidationError
from . import models

# Class do Formulario da Entregas
class EntregasForm(forms.ModelForm):
    fotos = forms.ImageField(
       widget=forms.FileInput(
           attrs={
               'accept': 'image/*',
               }
        )
    )
    # Este é uns dos campos do formulario, o jeito que voce que no formulario...
    apt = forms.CharField( 
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Numero apt',
                }
            ),label='Numero do apartamento')
    
    # Este é uns dos campos do formulario, o jeito que voce que no formulario...
    nome = forms.CharField(
        widget=forms.TextInput(
            attrs={'placeholder' : 'Destinario'}))
    

    # Meta é oque voce vai bota no formulario...
    class Meta :
        model = models.Entrega
        fields = (
            'apt', 'nome', 'receberam', 'fotos',
        )

    # essa Função é para verificar ser tem algum erro no formulario.
    def clean(self):
        # Validando ser tem algum error no campo 'apt'
        apt = self.cleaned_data.get('apt')
        if apt == '2500':
            self.add_error(
                'apt',
                ValidationError(
                    'Nao pode ser acima de 2400', code='invalid'
                )
            )
            return super().clean()
        
        # Este é a validaçao do 'nome'
        nome = self.cleaned_data.get('nome')
        if nome == 'abc':
            self.add_error(
                'nome', ValidationError(
                    'Não pode colocar abc', code='invalid'
                )
            )
            return super().clean()
        
# Class do Formulario da Ocorrencia
class OcorrenciaForm(forms.ModelForm):
    # adcionando o jeito que deseja coloca no campo 'nomeResp'
    nomeResp = forms.CharField(
        widget= forms.TimeInput(
            attrs= {
                'placeholder': 'Ronda/Porteiro seu Nome',
            }
        ), label='Nome'
    )
    # adcionando o jeito que deseja coloca no campo 'ocorrencia'
    ocorrencia = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder': 'Digite seu Livro de Ocorrencia aqui...',
            }
        )
    )

    # Meta é oque voce vai bota no formulario...
    class Meta:
        model = models.Ocorrencia
        fields = (
            'nomeResp', 'ocorrencia',
        )
    # essa Função é para verificar ser tem algum erro no formulario.
    def clean(self):
        # Este é a validaçao do 'nomeResp'
        nomeResp = self.cleaned_data.get('nomeResp')
        if nomeResp == 'abc':
            self.add_error(
                'nomeResp', ValidationError(
                    'Coloque seu Nome', code='invalid'
                )
            )
        return super().clean()