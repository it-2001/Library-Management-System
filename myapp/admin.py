from django.contrib import admin

from .models import *
# Register your models here.


admin.site.register(Autor)
admin.site.register(Nakladatelstvi)
admin.site.register(Kniha)
admin.site.register(Bydliste)
admin.site.register(Exemplar)
admin.site.register(Ctenar)

