from django.urls import path
from . import views

urlpatterns = [
    path('', views.render_pages, {'pagename': 'home'}),
    path('contact', views.render_contact_form, name='contact'),
    path('<str:pagename>', views.render_pages, name='home'),
]
