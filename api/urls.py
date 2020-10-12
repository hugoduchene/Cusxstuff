from django.urls import path, include

urlpatterns = [
    path('payements/', include('api.payements.urls'))
]
