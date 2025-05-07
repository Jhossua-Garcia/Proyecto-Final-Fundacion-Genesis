from django import forms
from .models import Auth

class FormularioRegistro(forms.ModelForm):
    password = forms.charFeld(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingresar Contraseña', 'class': 'form-control'}))
    
    confirmar_password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirmar Contraseña', 'class': 'form-control'}))
    
    class Meta:
        model = Auth
        fields = ('email', 'nombre', 'apellido', 'password', 'telefono')
        
    def __init__(self, *args, **kwargs):
        super(FormularioRegistro, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Ingresar Correo Electrónico'
        self.fields['nombre'].widget.attrs['placeholder'] = 'Ingresar Nombre'
        self.fields['apellido'].widget.attrs['placeholder'] = 'Ingresar Apellido'
        self.fields['telefono'].widget.attrs['placeholder'] = 'Ingresar Teléfono'
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
    
    def clean(self):
        limpiar_datos=super(FormularioRegistro, self).clean()
        password= limpiar_datos.get('password')
        confirmar_password= limpiar_datos.get('confirmar_password')

        if password != confirmar_password:
            raise forms.ValidationError(
                "Las contraseñas no coinciden, por favor verifique."
            )

