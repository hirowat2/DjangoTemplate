from django.db.models.signals import pre_save
from django.dispatch import receiver
from backend.segment.models import Segment
from django.utils.text import slugify

@receiver(pre_save, sender=Segment)
def product_pre_save(sender, instance, *args, **kwargs):
    # Example: Use the title of the segment to create the slug
    print(instance.title)  # Print the title of the segment to debug

    # Create a slug for the segment based on the title
    if instance.title:
        instance.slug = slugify(instance.title)
    else:
        # If no title, create a slug from the primary key
        instance.slug = slugify(str(instance.pk))
