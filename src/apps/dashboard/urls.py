from django.urls import path
from .views import (
    DashboardView,
    RedirectShortLinkView,
    DeleteShortLinkView,
    ShortLinkDetailView,
    GenerateQRCodeView,
    UpdateShortLinkView,
)

urlpatterns = [
    path('', DashboardView.as_view(), name='dashboard'),
    path('<str:short_code>/', RedirectShortLinkView.as_view(), name='redirect_short_link'),
    path('short-links/delete/<int:link_id>/', DeleteShortLinkView.as_view(), name='delete_short_link'),
    path('short-links/detail/<int:link_id>/', ShortLinkDetailView.as_view(), name='detail_short_link'),
    path('short-links/generate-qr/<int:link_id>/', GenerateQRCodeView.as_view(), name='generate_qr_code'),
    path('short-links/update/<int:link_id>/', UpdateShortLinkView.as_view(), name='update_short_link'),
]