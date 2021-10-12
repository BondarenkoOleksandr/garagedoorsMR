from django.db.models import CharField, TextField


def change_text(queryset):
    for model in queryset:
        model.firstscreen.title = model.firstscreen.title.replace('вЂ™', '\'')
        model.secondscreen.main_title = model.secondscreen.main_title.replace('вЂ™', '\'')
        model.firstscreen.description = model.firstscreen.description.replace('вЂ™', '\'')
        model.secondscreen.main_description = model.secondscreen.main_description.replace('вЂ™', '\'')
        model.description = model.description.replace('вЂ™', '\'')
        model.save()
