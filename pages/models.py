from django.db import models

from six import python_2_unicode_compatible

# Create your models here.


@python_2_unicode_compatible
class Page(models.Model):
    """ Custom dynamic page using the static site stylesheets """
    title = models.CharField(max_length=64)
    slug = models.SlugField(max_length=64)
    description = models.TextField(blank=True, help_text="This page description may appear in search engine results "
                                                         "and along with any links to this page.")

    body = models.TextField(help_text="Accepts raw text and/or HTML input")
    body_in_jumbo = models.BooleanField(default=False)
    noindex = models.BooleanField(default=False, verbose_name="Hide from search engines")
    sitemap = models.BooleanField(default=False, verbose_name="Include in Sitemap")
    sitemap_category = models.CharField(max_length=32, blank=True, null=True)

    css = models.TextField(blank=True, verbose_name="CSS")

    imgs = models.ManyToManyField('CarouselImg', blank=True)

    def __str__(self):
        return self.title


@python_2_unicode_compatible
class CarouselImg(models.Model):
    """ Image to be displayed as part of a carousel on a custom page """
    internal_name = models.CharField(max_length=64)
    img = models.ImageField(upload_to='carousel')
    href = models.ForeignKey('Page', on_delete=models.SET_NULL, null=True, blank=True)
    caption_title = models.CharField(max_length=64, null=True, blank=True)
    caption_desc = models.CharField(max_length=128, null=True, blank=True)

    def __str__(self):
        return self.internal_name
