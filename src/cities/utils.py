from autoslug.utils import slugify


def change_slug(models):
    for model in models:
        name = model.name
        model.slug = slugify(name)
        model.save()