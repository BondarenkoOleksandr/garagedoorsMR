from django.db import models

# Create your models here.


class SEOBase(models.Model):
    seo_title = models.CharField(max_length=500, null=True, blank=True)
    seo_description = models.TextField(max_length=500, null=True, blank=True)
    seo_canonical = models.URLField(null=True, blank=True)
    seo_robots = models.CharField(max_length=500, null=True, blank=True)
    seo_schema = models.TextField(null=True, blank=True)
    seo_og = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name_plural = "SEO"
