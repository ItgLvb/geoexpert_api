from django.urls import path, include
from .views import CadastralPlotView

app_name = 'api'


urlpatterns = [
    path('v1/cadastral/<str:cadastral_number>/', CadastralPlotView.as_view()),
]
