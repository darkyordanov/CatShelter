from django.urls import path

from cat_shelter.core.views import \
    home, about_us, faq, contact_us

urlpatterns = (
    path('', home, name='home'),
    path('about_us/', about_us, name='about_us'),
    path('faq/', faq, name='faq'),
    path('contact_us/', contact_us, name='contact_us'),
)
