# Generated by Django 3.0.6 on 2020-06-21 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('applicationBook', '0003_auto_20200621_1202'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pdf_book',
            field=models.FileField(default='true', upload_to='pdf/', verbose_name='ссылка pdf'),
        ),
        migrations.AlterField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='', max_length=100, verbose_name='Автор'),
        ),
        migrations.AlterField(
            model_name='book',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='book',
            name='image_book',
            field=models.ImageField(blank=True, upload_to='image/', verbose_name='ссылка'),
        ),
    ]
