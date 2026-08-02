from django.db import migrations


def create_kids_categories(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    for item in (
        {'name': 'Boy', 'slug': 'boy', 'sort_order': 10},
        {'name': 'Girl', 'slug': 'girl', 'sort_order': 20},
    ):
        Category.objects.get_or_create(
            slug=item['slug'],
            defaults={
                'name': item['name'],
                'parent': None,
                'is_active': True,
                'sort_order': item['sort_order'],
            },
        )


def remove_kids_categories(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    Category.objects.filter(slug__in=['boy', 'girl'], parent__isnull=True).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_kids_categories, remove_kids_categories),
    ]
