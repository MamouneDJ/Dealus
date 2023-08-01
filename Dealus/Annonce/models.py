from django.db import models
from Utilisateur.models import CustomUser
from django.urls import reverse

# Create your models here.
class Annonce(models.Model):
    """Info"""
    title = models.CharField(max_length=100)
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='annonce')
    description = models.TextField()
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    fixed_price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True,default=0)
    min_price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True,default=0)
    max_price = models.DecimalField(max_digits=10, decimal_places=0, null=True, blank=True,default=0)
    """"analystic"""
    date_ads_posted = models.DateTimeField(auto_now_add=True)
    click_count = models.PositiveIntegerField(default=0)
    clicks_timestamp = models.DateTimeField(blank=True, null=True, default=None)
    is_favorites = models.BooleanField(default=False)
    is_vip = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('annonce_detail', args=[str(self.id)])
    def __str__(self):
        return self.title
