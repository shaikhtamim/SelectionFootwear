from django.db import models


class VisitorLead(models.Model):
    name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=150)
    mobile = models.CharField(max_length=15, unique=True)

    ip_address = models.GenericIPAddressField(null=True, blank=True)

    browser = models.CharField(max_length=100, blank=True)
    device = models.CharField(max_length=100, blank=True)
    operating_system = models.CharField(max_length=100, blank=True)

    user_agent = models.TextField(blank=True)

    visit_count = models.PositiveIntegerField(default=1)

    last_visit = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-last_visit']
        verbose_name = "Visitor Lead"
        verbose_name_plural = "Visitor Leads"

    def __str__(self):
        return f"{self.name} - {self.shop_name}"