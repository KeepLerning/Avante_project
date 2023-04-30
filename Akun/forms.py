from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class FormPendaftaran(UserCreationForm):
    Nomor_phone = forms.IntegerField()

    class Meta:
        model = User
        fields = [
            'username',
            'password1',
            'password2',
            'email',
            'Nomor_phone',
        ]

    # def seve(self, commit=True):
    #     user = super(FromPendaftaran, self).seve(commit=False)
    #     user.Nomor_phone = self.clean_data['Nomor_phone']
    #     if commit:
    #         user.save()
    #     return user




