import datetime
import random

from django.utils import timezone

from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework_jwt.serializers import VerifyJSONWebTokenSerializer
from autoslug.utils import slugify


class ExtendedEncoder(DjangoJSONEncoder):
    def default(self, o):
        if isinstance(o, ImageFieldFile):
            return str(o)
        else:
            return super().default(o)


def get_user_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip


def get_now() -> datetime.datetime:
    return timezone.now()


def add_images_path(request, model, data):
    if model.firstscreen.image:
        data['first_screen'].update({'image': request.build_absolute_uri(model.firstscreen.image.url)})
    if model.thirdscreen.image:
        data['third_screen'].update({'image': request.build_absolute_uri(model.thirdscreen.image.url)})

    return data


def queryset_pagination(request, queryset):
    if not request.GET.get('per_page', False):
        return queryset

    try:
        page = int(request.GET.get('page', 0))
        per_page = int(request.GET.get('per_page', 0))
    except:
        raise ValueError('Int value expected but str given')

    start = page * per_page
    end = start + per_page

    if start > len(queryset) or end > len(queryset):
        return queryset

    return queryset[start:end]


def get_user_by_jwt(request):
    token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
    data = {'token': token}
    try:
        valid_data = VerifyJSONWebTokenSerializer().validate(data)
        user = valid_data['user']
        request.user = user
        return user
    except ValidationError as v:
        print("validation error", v)
        return v.args


def change_slug(models):
    for model in models:
        name = model.name
        model.slug = slugify(name)
        model.save()


def change_rating(models):
    for model in models:
        model.rating = random.randint(4, 5)
        model.count_votes = random.randint(10, 45)
        model.save()


def change_text(models):
    for model in models:
        model.firstscreen.title = model.firstscreen.title.replace('вЂ™', '\'').replace('вЂ”', '—')
        model.firstscreen.description = model.firstscreen.description.replace('вЂ™', '\'').replace('вЂ”', '—')
        model.secondscreen.main_title = model.secondscreen.main_title.replace('вЂ™', '\'').replace('вЂ”', '—')
        model.secondscreen.main_description = model.secondscreen.main_description.replace('вЂ™', '\'').replace('вЂ”', '—')
        model.secondscreen.sec_title = model.secondscreen.sec_title.replace('вЂ™', '\'').replace('вЂ”', '—')
        model.secondscreen.sec_description = model.secondscreen.sec_description.replace('вЂ™', '\'').replace('вЂ”', '—')
        model.thirdscreen.main_description = model.thirdscreen.main_description.replace('вЂ™', '\'').replace('вЂ”', '—')
        model.thirdscreen.sec_title = model.thirdscreen.sec_title.replace('вЂ™', '\'').replace('вЂ”', '—')
        model.thirdscreen.sec_description = model.thirdscreen.sec_description.replace('вЂ™', '\'').replace('вЂ”', '—')
        model.thirdscreen.thrd_title = model.thirdscreen.thrd_title.replace('вЂ™', '\'').replace('вЂ”', '—')
        model.thirdscreen.thrd_description = model.thirdscreen.thrd_description.replace('вЂ™', '\'').replace('вЂ”', '—')
        model.save()
        model.firstscreen.save()
        model.secondscreen.save()
        model.thirdscreen.save()


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'per_page'
    max_page_size = 10000