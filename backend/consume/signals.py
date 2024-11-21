from django.utils.text import slugify


def consume_pre_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)
