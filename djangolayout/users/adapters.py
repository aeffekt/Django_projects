from allauth.account.adapter import DefaultAccountAdapter
from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.contrib.auth import get_user_model

class MyAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        # Sobrescribe esta función si necesitas personalizar la forma en que se guarda el usuario
        return super().save_user(request, user, form, commit)

class MySocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        # Evita que se registre un nuevo usuario si ya existe uno con el mismo correo
        if sociallogin.is_existing:
            return
        
        email_address = sociallogin.account.extra_data.get('email')
        if email_address:            
            try:
                user = get_user_model().objects.get(email=email_address)
                # Asocia la cuenta social con el usuario existente
                sociallogin.connect(request, user)
            except get_user_model().DoesNotExist:
                pass  # No hay usuario con ese email, procede con el registro normal