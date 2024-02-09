from django.apps import AppConfig


class UsersConfig(AppConfig):    
    name = 'users'

    def ready(self):            # importar las signals (de crear profile al crear User)        
        import users.signals    # modo recomendado por la documentacion de Django