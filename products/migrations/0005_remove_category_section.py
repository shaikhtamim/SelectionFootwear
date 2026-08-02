from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_set_category_sections'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['sort_order', 'name'], 'verbose_name_plural': 'categories'},
        ),
        migrations.RemoveField(
            model_name='category',
            name='section',
        ),
    ]
