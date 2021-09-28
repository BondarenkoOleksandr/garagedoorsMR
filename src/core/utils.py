from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields.files import ImageFieldFile


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
