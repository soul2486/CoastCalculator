from django.urls import path

from . import views

# app_name = 'coca'

urlpatterns = [
    path('', views.HomeView.as_view() , name="Home"),
    path('appliances_coca', views.AppliancesView.as_view() , name="appliances"),
    # path('bills_coca', views.BillsView.as_view() , name="bills_coca"),
    path('UserInfo/<str:email>', views.InfoUserView.as_view() , name="user_info"),
    path('get_coast/<int:pk>', views.GetCoastView.as_view() , name="get_coast"),
    path('from/', views.FromView, name="from"),
    path('Apropos/', views.Apropos, name="apropos"),
    path('Contact/', views.Contact, name="contact"),
    path('checkuser/', views.checkUserView.as_view(), name="check_user"),
    path('get_appliance_power/<int:appliance_id>/', views.get_appliance_power, name='get_appliance_power'),

        
]

