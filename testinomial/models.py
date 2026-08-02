from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Testimonial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Customer Name")
    location = models.CharField(
        max_length=100, 
        blank=True, 
        null=True, 
        help_text="e.g. Ahmedabad, Gujarat"
    )
    image = models.ImageField(upload_to="testimonials/", blank=True, null=True)
    
    # YAHAN CHANGE KIYA HAI 👇
    review_rate = models.DecimalField(
        max_digits=2, 
        decimal_places=1, 
        default=5.0, 
        validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],
        help_text="Enter rating between 1.0 and 5.0 (e.g. 3.5)"
    )
    
    description = models.TextField(verbose_name="Review Text")
    is_active = models.BooleanField(default=True, help_text="Designates whether this review is visible on the site.")
    sort_order = models.PositiveIntegerField(default=0, help_text="Lower number appears first")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "sf_testimonial"
        ordering = ["sort_order", "id"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self):
        return f"{self.name} ({self.review_rate} Stars)"

    
    @property
    def get_stars(self):
        full_stars = int(self.review_rate)
        # Agar decimal 0.5 ya usse zyada hai, toh 1 half star
        half_star = 1 if (self.review_rate % 1) >= 0.5 else 0 
        empty_stars = 5 - full_stars - half_star
        
        return {
            'full': range(full_stars),
            'half': range(half_star),
            'empty': range(empty_stars)
        }