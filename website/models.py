from django.db import models

# Aapke baaki existing models yahan honge (Product, Gallery, etc.)

class Lead(models.Model):
    name = models.CharField(max_length=100)
    shop_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Lead"
        verbose_name_plural = "Leads"

    def __str__(self):
        return f"{self.name} - {self.shop_name}"