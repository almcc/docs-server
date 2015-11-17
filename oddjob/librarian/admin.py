from django.contrib import admin
from .models import Collection, Product, Release, Artifact

admin.site.register(Collection)
admin.site.register(Product)
admin.site.register(Release)
admin.site.register(Artifact)
