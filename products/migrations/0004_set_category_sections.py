from django.db import migrations


def set_category_sections(apps, schema_editor):
    Category = apps.get_model('products', 'Category')
    # Kept for history only — section field is removed in 0005
    if hasattr(Category, 'section') or 'section' in [f.name for f in Category._meta.local_fields]:
        Category.objects.filter(slug__in=['boy', 'boys', 'girl', 'girls']).update(
            section='kids',
            parent=None,
        )
        Category.objects.filter(slug='women').update(section='women')
        Category.objects.filter(parent__slug='women').update(section='women')


def noop(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_category_section'),
    ]

    operations = [
        migrations.RunPython(set_category_sections, noop),
    ]
