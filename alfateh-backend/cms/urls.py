from django.urls import path
from .views import (
    HeroSectionByLocaleView,
    AboutSectionByLocaleView,
    ServiceListByLocaleView,
    ServiceDetailByLocaleAndSlugView,
    FAQListByLocaleView,
    FooterInfoByLocaleView,
    ContactMessageCreateView,
)

urlpatterns = [
    path("hero/<str:locale>/", HeroSectionByLocaleView.as_view(), name="hero-by-locale"),
    path("about/<str:locale>/", AboutSectionByLocaleView.as_view(), name="about-by-locale"),
    path("services/<str:locale>/", ServiceListByLocaleView.as_view(), name="services-by-locale"),
    path(
        "services/<str:locale>/<slug:slug>/",
        ServiceDetailByLocaleAndSlugView.as_view(),
        name="service-detail-by-locale",
    ),
    path("faq/<str:locale>/", FAQListByLocaleView.as_view(), name="faq-by-locale"),
    path("footer/<str:locale>/", FooterInfoByLocaleView.as_view(), name="footer-by-locale"),
    path("contact/", ContactMessageCreateView.as_view(), name="contact-create"),
]

