from django.contrib import admin

# Register your models here.

from crud.models import Pessoa

admin.site.register(Pessoa)