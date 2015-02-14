from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import ArchiveIndexView

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'meusite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', ArchiveIndexView.as_view(date_field='publicacao', queryset=Artigo.objects.all())),
)
