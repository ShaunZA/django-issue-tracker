"""issue_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from accounts import urls as urls_accounts
from tickets import urls as urls_tickets
from search import urls as urls_search
from tickets.views import all_tickets, one_ticket
from accounts.views import index
from django.conf import settings
from payment.views import payment_form, checkout
from django.conf.urls.static import static 

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', all_tickets, name='index'),
    url(r'^accounts/', include(urls_accounts)),
    url(r'^tickets/', include(urls_tickets)),
    url(r'^search/', include(urls_search)),
    url(r'^payment-form$', payment_form, name="payment_form"),
    url(r"^checkout$", checkout, name="checkout_page")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)