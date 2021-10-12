import datetime

from django.contrib.auth.models import User
from django.db import models
from django.db.models import Avg

from django.core.exceptions import ValidationError
from taggit.managers import TaggableManager


# Create your models here.
from seo.models import SEOBase


class Article(models.Model):
    RATING_COUNT = [(i, i) for i in range(1, 6)]
    author = models.ForeignKey(User, related_name='poster', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(default='default-picture.png', upload_to='articles/', null=True)
    title = models.CharField(max_length=100)
    excerpt = models.TextField(max_length=1000, null=True)
    slug = models.SlugField(
        max_length=100,
        editable=False,
        unique=True,
    )
    tags = TaggableManager()
    publish_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='article_like', editable=False)

    def clean(self):
        if not self.slug and Article.objects.filter(title__iexact=self.title):
            raise ValidationError('Article with this title already exists')

    def __str__(self):
        return self.title + ' - ' + self.author.username

    def number_of_likes(self):
        return self.likes.count()

    @property
    def views_count(self):
        return ArticleView.objects.filter(article=self).count()

    def get_slug(self):
        return self.slug


class ArticleView(models.Model):
    IPAddress = models.GenericIPAddressField(default="45.243.82.169")
    article = models.ForeignKey('Article', on_delete=models.CASCADE)

    def __str__(self):
        return '{0} in {1} post'.format(self.IPAddress, self.article.title)


class ArticleRating(models.Model):
    STARS = (
        (1, 'Very bad'),
        (2, 'Bad'),
        (3, 'Normal'),
        (4, 'Good'),
        (5, 'Excellent'),
    )
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='article_rating')
    rating = models.SmallIntegerField(choices=STARS, null=True, default=STARS[0])
    IPAddress = models.GenericIPAddressField(default="45.243.82.169")

    @property
    def get_rating(self):
        avg_rating = ArticleRating.objects.aggregate(Avg('rating'))
        return int(avg_rating['rating__avg'])

    @property
    def get_count(self):
        return ArticleRating.objects.filter(article=self.article).count()


class Comment(models.Model):
    STATUS_LEVEL = [
        (0, 'Moderation'),
        (1, 'Published'),
        (2, 'Archived'),
    ]
    user = models.ForeignKey(User, related_name='author', on_delete=models.SET_NULL, null=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='subcomments')

    status = models.IntegerField(choices=STATUS_LEVEL, default=0)

    text = models.CharField(max_length=250)
    pub_date = models.DateField('date published', auto_now_add=True)

    def __str__(self):
        return self.text[0:15] + ' - ' + self.article.title + ' - ' + self.user.username


class Paragraphs(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='articles/par/', null=True, blank=True)
    quote = models.TextField(max_length=250, blank=True, null=True)
    article = models.ForeignKey(
        to=Article,
        null=False,
        on_delete=models.CASCADE,
        verbose_name='Абзацы:',
        related_name='paragraphs',
    )

    class Meta:
        verbose_name_plural = "Paragraphs"


class SEOArticles(SEOBase):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, null=True, related_name='seo')
