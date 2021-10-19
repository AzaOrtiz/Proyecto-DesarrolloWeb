from django.contrib import admin
from .models import accesorio, computadora, marca, tipoacces, tipocompu

# Register your models here.
admin.site.register(computadora)
admin.site.register(accesorio)
admin.site.register(marca)
admin.site.register(tipocompu)
admin.site.register(tipoacces)