from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Avg
import uuid
from django_quill.fields import QuillField
from django.utils.text import slugify


# Create your models here.


class Article(models.Model):
    RATING_COUNT = [(i, i) for i in range(1, 6)]
    author = models.ForeignKey(User, related_name='poster', on_delete=models.SET_NULL, null=True)
    image = models.ImageField(default='default-picture.png', upload_to='articles/', null=True)
    title = models.CharField(max_length=100)
    content = QuillField()
    slug = models.SlugField(
        max_length=100,
        editable=False,
        unique=True,
        default=slugify(title)
    )
    publish_date = models.DateField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name='article_like', editable=False)

    def clean(self):
        if not self.slug and Article.objects.filter(title=self.title):
            raise ValidationError('Article with this title already exists')

    def __str__(self):
        return self.title + ' - ' + self.author.username

    def number_of_likes(self):
        return self.likes.count()

    @property
    def views_count(self):
        return ArticleViews.objects.filter(article=self).count()

    def get_slug(self):
        return self.slug


class ArticleViews(models.Model):
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
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    rating = models.SmallIntegerField(choices=STARS)

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
    pub_date = models.DateTimeField('date published', auto_now_add=True)

    def __str__(self):
        return self.text[0:15] + ' - ' + self.article.title + ' - ' + self.user.username
