from django.db.models import CharField, Model
from django_extensions.db.fields import AutoSlugField

class Tag(Model):
    name = CharField(max_length=31, unique=True)
    slug = AutoSlugField(
        help_text = "A label for URL config.",
        max_length = 31,
        populate_from=["name"]
    )
    def __str__(self):
        return self.name