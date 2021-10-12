from django.db.models import CharField, TextField


def change_text(queryset):
    for model in queryset:
        model.firstscreen.title = model.firstscreen.title.repace('вЂ™', '\'')
        model.secondscreen.main_title = model.secondscreen.main_title.repace('вЂ™', '\'')
        model.firstscreen.description = model.firstscreen.description.repace('вЂ™', '\'')
        model.secondscreen.main_description = model.secondscreen.main_description.repace('вЂ™', '\'')
        model.description = model.description.repace('вЂ™', '\'')
        model.save()
