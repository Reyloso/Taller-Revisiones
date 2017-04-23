from django.contrib import admin
from .models import Cliente, Auto, Consecionario, Revision
# Register your models here.


class cliente (admin.ModelAdmin):
	list_display = ['nid', 'nombre','primer_apellido','segundo_apellido','telefono','auto']
	class Meta:
		model = Cliente

class auto (admin.ModelAdmin):

	list_display = ['matricula', 'marca','tipo','modelo','consecionario','color']
	class Meta:
		model = Auto

class consecionario (admin.ModelAdmin):

	list_display = ['nit','nombre','telefono']
	class Meta:
		model = Consecionario

class revision (admin.ModelAdmin):

	list_display = ['id','auto','filtro','aceite','frenos','motor']
	class Meta:
		model = Revision


admin.site.register(Cliente,cliente)
admin.site.register(Auto,auto)
admin.site.register(Consecionario,consecionario)
admin.site.register(Revision,revision)
