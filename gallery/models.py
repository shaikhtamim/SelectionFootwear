from django.db import models


class Gallery(models.Model):
    title = models.CharField(max_length=255)
    main_image = models.ImageField(upload_to='gallery/main/')
    sort_order = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)

    # NEW FIELD
    show_on_home = models.BooleanField(
        default=False,
        verbose_name="Show on Home Page"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "sf_gallery"
        ordering = ["sort_order", "id"]

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    gallery = models.ForeignKey(
        Gallery,
        on_delete=models.CASCADE,
        related_name="gallery_images"
    )

    image_path = models.ImageField(upload_to='gallery/images/')

    class Meta:
        db_table = "sf_gallery_images"

    def __str__(self):
        return f"{self.gallery.title} Image"