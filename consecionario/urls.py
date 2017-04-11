
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^lista/autos/$', 'venta.views.lista_autos', name='lista-autos'),
    url(r'^$', 'core.views.inicio', name='inicio'),
    url(r'^nuevo/auto/$', 'venta.views.crear_auto', name='nuevo-auto'),
    url(r'^eliminar/auto/(?P<id>\d+)', 'venta.views.eliminar_auto', name='eliminar-auto'),
    url(r'^modificar/auto/(?P<id>\d+)', 'venta.views.modificar_auto', name='modificar-auto'),
    url(r'^lista/cliente/$', 'venta.views.lista_cliente', name='lista-cliente'),
    url(r'^nuevo/cliente/$', 'venta.views.crear_cliente', name='nuevo-cliente'),
    url(r'^modificar/cliente/(?P<nid>\d+)', 'venta.views.modificar_cliente', name='modificar-cliente'),
    url(r'^eliminar/cliente/(?P<nid>\d+)', 'venta.views.eliminar_cliente', name='eliminar-cliente'),
    url(r'^lista/consecionario/$', 'venta.views.lista_consecionario', name='lista-consecionario'),
    url(r'^nuevo/consecionario/$', 'venta.views.crear_consecionario', name='nuevo-consecionario'),
    url(r'^modificar/consecionario/(?P<nit>\d+)', 'venta.views.modificar_consecionario', name='modificar-consecionario'),
    url(r'^eliminar/consecionario/(?P<nit>\d+)', 'venta.views.eliminar_consecionario', name='eliminar-consecionario'),
    url(r'^lista/revision/$', 'venta.views.lista_revision', name='lista-revision'),
    url(r'^nueva/revision/$', 'venta.views.crear_revision', name='nueva-revision'),
    url(r'^lista/revision/auto/(?P<id>\d+)', 'venta.views.lista_revision_auto', name='lista-revision-auto'),
    url(r'^eliminar/revision/(?P<id>\d+)', 'venta.views.eliminar_revision', name='eliminar-revision'),
    url(r'^modificar/revision/(?P<id>\d+)', 'venta.views.modificar_revision', name='modificar-revision'),



]
