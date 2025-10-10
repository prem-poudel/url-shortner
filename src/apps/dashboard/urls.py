from django.urls import path
from .views import DashboardView, RedirectShortLinkView

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('<str:short_code>/', RedirectShortLinkView.as_view(), name='redirect_short_link'),
]