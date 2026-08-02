from django.db import models


class Contact(models.Model):

    full_name = models.CharField(max_length=100)

    email = models.EmailField()

    subject = models.CharField(
        max_length=200,
        blank=True,
        null=True
    )

    message = models.TextField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.full_name