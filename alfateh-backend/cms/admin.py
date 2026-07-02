from django.contrib import admin
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


@admin.register(HeroSection)
class HeroSectionAdmin(admin.ModelAdmin):
    list_display = ("locale", "title", "primary_button_text")
    list_filter = ("locale",)
    search_fields = ("title", "subtitle")


@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ("locale", "title")
    list_filter = ("locale",)
    search_fields = ("title", "body")


class ServiceDetailInline(admin.StackedInline):
    model = ServiceDetail
    extra = 0


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("locale", "name", "slug")
    list_filter = ("locale",)
    search_fields = ("name", "short_description", "slug")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [ServiceDetailInline]


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("locale", "question")
    list_filter = ("locale",)
    search_fields = ("question", "answer")


class SocialLinkInline(admin.TabularInline):
    model = SocialLink
    extra = 1


@admin.register(FooterInfo)
class FooterInfoAdmin(admin.ModelAdmin):
    list_display = ("locale", "company_name", "phone", "email")
    list_filter = ("locale",)
    inlines = [SocialLinkInline]


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "created_at")
    search_fields = ("name", "phone", "message")
    readonly_fields = ("created_at",)

