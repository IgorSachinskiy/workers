from django import forms
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class RegisterForm(forms.ModelForm):
      password_confirmation = forms.CharField(label='Подтверждение пароля', max_length=128)

      class Meta:
          model = UserModel
          fields = ('email', 'username', 'password')


      def clean(self):
          data = self.cleaned_data
          if data['password'] != data['password_confirmation']:
              raise forms.ValidationError('Пароли не совпадают')
          return data


      def save(self, commit=True):
          value = self.instance.password
          self.instance.set_password(value)
          return super().save(commit=commit)
