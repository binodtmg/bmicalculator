from django.urls import path
from home.views import  bmiuserlist, bmiform, bmi_edit, bmi_delete,  send_confirm_email

app_name = "home"

urlpatterns = [
    # path('', bmi, name="bmi"),
    path('bmiuserlist/', bmiuserlist, name="bmiuserlist"),
    path('bmiform/', bmiform, name="bmiform"),
    path('bmi-edit/<int:id>/', bmi_edit, name="bmi_edit"),
    path('bmi-delete/<int:id>/', bmi_delete, name="bmi_delete"),
    # path('mailform/', mailform, name="mailform"),
    path("send-mail/",send_confirm_email, name="sendmail")
]