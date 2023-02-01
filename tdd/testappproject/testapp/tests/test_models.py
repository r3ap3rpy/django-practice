from django.test import TestCase
from django.db import IntegrityError
from ..models import Tag

class TagModelTestDemo(TestCase):
    def test_concrete_fields(self):
        field_names = [field.name for field in Tag._meta.get_fields()]
        expected_field_names = ["id","name","slug"]
        self.assertEqual(field_names,expected_field_names)

    def test_name_uniqueness(self):
        kwargs = dict(name='a')
        Tag.objects.create(**kwargs)
        with self.assertRaises(IntegrityError):
            Tag.objects.create(**kwargs)

    def test_list_order(self):
        Tag.objects.create(name = "b")
        Tag.objects.create(name = "D")
        Tag.objects.create(name = "c")
        Tag.objects.create(name = "a")
        tag_name_list = list(
            Tag.objects.values_list("name",flat=True)
        )
        expected_name_list = ["D","a","b","c"]
        self.assertEqual(tag_name_list,expected_name_list)
    
    def test_str(self):
        t = Tag.objects.create(name="django")
        self.assertEqual(str(t),"django")