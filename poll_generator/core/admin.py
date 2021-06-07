from django.contrib import admin
from core import models


# Registra models, para que seja possível visualizar e manipular
# os dados pela tela do Django Admin
admin.site.register(models.Poll)
admin.site.register(models.Option)
admin.site.register(models.VotesControl)
