from django.db import models

# Create your models here.


class CryptoList(models.Model):
    RATINGS = (
        ('1', 'MILLION'),
        ('2', 'BILLION'),
        ('3', 'TRILLION'),
    )
    name = models.CharField(max_length=500)
    website = models.URLField(max_length=500)
    symbol_name = models.CharField(max_length=100)
    slugfield = models.SlugField(max_length=700)
    market_Cap = models.PositiveIntegerField()
    currencylength = models.CharField(max_length=1000, choices=RATINGS)
    Price = models.DecimalField(decimal_places=5, max_digits=1000000000000000)
    circulating_Supply = models.DecimalField(
        decimal_places=5, max_digits=1000000000000000)
    updated_date = models.DateField(auto_now_add=True)
    # gallery_img = models.ImageField(default='default3.jpeg', blank=True)
    # thumbimg = models.ImageField(default='default.jpeg', blank=True)

    def __str__(self):
        return self.name
