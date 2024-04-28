# Generated by Django 4.1 on 2024-04-28 13:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Material', 'verbose_name_plural': 'Materials'},
        ),
        migrations.AlterModelOptions(
            name='usermaterial',
            options={'verbose_name': 'UserMaterial', 'verbose_name_plural': 'UserMaterials'},
        ),
        migrations.RenameField(
            model_name='usermaterial',
            old_name='book',
            new_name='material',
        ),
        migrations.AddField(
            model_name='material',
            name='description',
            field=models.TextField(blank=True, max_length=6000, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='material',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='material',
            name='rating',
            field=models.DecimalField(blank=True, decimal_places=2, default=None, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=models.ImageField(blank=True, default='media/default_avatar.jpg', upload_to='profile_avatars'),
        ),
    ]
