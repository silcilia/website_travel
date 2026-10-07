from django.db import models


class BookingInquiry(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    package = models.CharField(max_length=120, blank=True)
    message = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Booking Inquiry'
        verbose_name_plural = 'Booking Inquiries'

    def __str__(self):
        return f'{self.name} - {self.phone}'
