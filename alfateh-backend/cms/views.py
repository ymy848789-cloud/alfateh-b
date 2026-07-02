from rest_framework import generics, permissions
from .models import (
    HeroSection,
    AboutSection,
    Service,
    FAQ,
    FooterInfo,
    ContactMessage,
)
from .serializers import (
    HeroSectionSerializer,
    AboutSectionSerializer,
    ServiceSerializer,
    FAQSerializer,
    FooterInfoSerializer,
    ContactMessageSerializer,
)


class HeroSectionByLocaleView(generics.RetrieveAPIView):
    serializer_class = HeroSectionSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        locale = self.kwargs.get("locale", "ar")
        return HeroSection.objects.filter(locale=locale).first()


class AboutSectionByLocaleView(generics.RetrieveAPIView):
    serializer_class = AboutSectionSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        locale = self.kwargs.get("locale", "ar")
        return AboutSection.objects.filter(locale=locale).first()


class ServiceListByLocaleView(generics.ListAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        locale = self.kwargs.get("locale", "ar")
        return Service.objects.filter(locale=locale)


class ServiceDetailByLocaleAndSlugView(generics.RetrieveAPIView):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        locale = self.kwargs.get("locale", "ar")
        slug = self.kwargs.get("slug")
        return Service.objects.filter(locale=locale, slug=slug).first()


class FAQListByLocaleView(generics.ListAPIView):
    serializer_class = FAQSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        locale = self.kwargs.get("locale", "ar")
        return FAQ.objects.filter(locale=locale)


class FooterInfoByLocaleView(generics.RetrieveAPIView):
    serializer_class = FooterInfoSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        locale = self.kwargs.get("locale", "ar")
        return FooterInfo.objects.filter(locale=locale).first()


class ContactMessageCreateView(generics.CreateAPIView):
    serializer_class = ContactMessageSerializer
    permission_classes = [permissions.AllowAny]

    def perform_create(self, serializer):
        serializer.save()

