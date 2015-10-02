from django.db import models


class Collection(models.Model):
    name = models.CharField(max_length=200, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200, unique=True)
    collections = models.ManyToManyField(Collection, blank=True, related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Release(models.Model):
    name = models.CharField(max_length=200)
    product = models.ForeignKey(Product, related_name='releases')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'product')

    def __str__(self):
        return '{}-{}'.format(self.product.name, self.name)


class Artifact(models.Model):
    name = models.CharField(max_length=200)
    release = models.ForeignKey(Release, related_name='artifacts')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('name', 'release')

    def __str__(self):
        return '{}-{} ({})'.format(self.release.product.name, self.release.name, self.name)
