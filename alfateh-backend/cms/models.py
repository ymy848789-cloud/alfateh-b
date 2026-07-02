from django.db import models


LOCALE_CHOICES = [
    ("ar", "Arabic"),
    ("en", "English"),
]


class HeroSection(models.Model):
    locale = models.CharField(max_length=2, choices=LOCALE_CHOICES)
    title = models.CharField(max_length=255)
    subtitle = models.TextField()
    primary_button_text = models.CharField(max_length=100)
    primary_button_link = models.CharField(max_length=255)

    def __str__(self):
        return f"Hero ({self.locale}) - {self.title}"


class AboutSection(models.Model):
    locale = models.CharField(max_length=2, choices=LOCALE_CHOICES)
    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
        return f"About ({self.locale}) - {self.title}"


class Service(models.Model):
    locale = models.CharField(max_length=2, choices=LOCALE_CHOICES)
    slug = models.SlugField()
    name = models.CharField(max_length=255)
    short_description = models.TextField()
    icon = models.CharField(max_length=100, blank=True)

    class Meta:
        unique_together = ("locale", "slug")

    def __str__(self):
        return f"{self.locale} - {self.name}"


class ServiceDetail(models.Model):
    service = models.OneToOneField(Service, on_delete=models.CASCADE, related_name="detail")
    subtitle = models.TextField(blank=True)
    long_description = models.TextField(blank=True)
    highlights = models.TextField(
        blank=True,
        help_text="كل سطر يمثل نقطة مميزة (Highlight) منفصلة.",
    )
    stats = models.TextField(
        blank=True,
        help_text="يمكن تخزين إحصائيات بشكل JSON أو نص منسق.",
    )
    plans = models.TextField(
        blank=True,
        help_text="يمكن تخزين الباقات (Plans) بشكل JSON أو نص منسق.",
    )
    extra_sections = models.TextField(
        blank=True,
        help_text="نص منسق أو JSON لأقسام إضافية في صفحة الخدمة.",
    )
    cta_title = models.CharField(max_length=255, blank=True)
    cta_description = models.TextField(blank=True)
    cta_button_text = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return f"Details for {self.service.name} ({self.service.locale})"


class FAQ(models.Model):
    locale = models.CharField(max_length=2, choices=LOCALE_CHOICES)
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return f"FAQ ({self.locale}) - {self.question}"


class FooterInfo(models.Model):
    locale = models.CharField(max_length=2, choices=LOCALE_CHOICES)
    company_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=50)
    email = models.EmailField()
    copyright_text = models.CharField(max_length=255)

    def __str__(self):
        return f"Footer ({self.locale}) - {self.company_name}"


class SocialLink(models.Model):
    footer = models.ForeignKey(FooterInfo, on_delete=models.CASCADE, related_name="social_links")
    platform = models.CharField(max_length=50)
    url = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.platform} - {self.url}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.phone}"

