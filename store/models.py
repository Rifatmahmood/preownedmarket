from django.db import models

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=250, db_index=True)
    slug = models.SlugField(max_length=250, unique=True)
    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name 
    # def get_absolute_url(self):
    #     return reverse('list-category', args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=250)
    brand = models.CharField(max_length=250, default='un-brand')
    description = models.TextField(blank=True)
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    img = models.ImageField()
    

    class Meta:
        verbose_name_plural = 'products'

    def __str__(self):
        return self.title 
