from rest_framework import serializers
from .models import (
    HeroSection,
    AboutSection,
    Service,
    ServiceDetail,
    FAQ,
    FooterInfo,
    SocialLink,
    ContactMessage,
)


class HeroSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSection
        fields = "__all__"


class AboutSectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutSection
        fields = "__all__"


class ServiceDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceDetail
        fields = "__all__"


class ServiceSerializer(serializers.ModelSerializer):
    detail = ServiceDetailSerializer(read_only=True)

    class Meta:
        model = Service
        fields = "__all__"


class FAQSerializer(serializers.ModelSerializer):
    class Meta:
        model = FAQ
        fields = "__all__"


class SocialLinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialLink
        fields = "__all__"


class FooterInfoSerializer(serializers.ModelSerializer):
    social_links = SocialLinkSerializer(many=True, read_only=True)

    class Meta:
        model = FooterInfo
        fields = "__all__"


class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"

