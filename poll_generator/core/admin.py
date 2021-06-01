from django.contrib import admin
from core import models


admin.site.register(models.Poll)
admin.site.register(models.Option)
admin.site.register(models.VotesControl)
