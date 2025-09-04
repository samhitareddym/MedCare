"""medmart URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from medmartapp import views as m


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',m.index,name="index"),
    path('about/',m.about,name="about"),
    path('services/',m.services,name="services"),
    path('contact/',m.contact,name="contact"),
    path('contact_page/',m.contact_page,name="contact_page"),
    path('client/',m.client,name="client"),
    path('staff/',m.staff,name="staff"),
    path('client_reg/',m.client_reg,name="client_reg"),
    path('client_register/',m.client_register,name="client_register"),
    path('customer_login/',m.customer_login,name="customer_login"),
    path('client_profile/',m.client_profile,name="client_profile"),
    path('client_details/',m.client_details,name="client_details"),
    path('client_logout/',m.client_logout,name="client_logout"),
    path('client_changepassword/',m.client_changepassword,name="client_changepassword"),
    path('client_delete/<str:email>',m.client_delete,name="client_delete"),
    path('client_edit/<str:email>',m.client_edit,name="client_edit"),
    path('client_update/',m.client_update,name="client_update"),
    path('client_view_service/',m.client_view_service,name="client_view_service"),
    path('book_slot/',m.book_slot,name="book_slot"),
    path('viewcart/',m.viewcart,name="viewcart"),
    path('addcart/<int:id>',m.addcart,name="addcart"),
    path('fake/',m.fake,name="fake"),



# staff urls

    path('staff_login/',m.staff_login,name="staff_login"),
    path('staff_profile/',m.staff_profile,name="staff_profile"),
    path('staff_logout/',m.staff_logout,name="staff_logout"),
    path('staff_view_cart/',m.staff_view_cart,name="staff_view_cart"),
    path('approve_slot/<str:service_id>',m.approve_slot,name="approve_slot"),
    path('reject_slot/<str:service_id>',m.reject_slot,name="reject_slot"),

]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)