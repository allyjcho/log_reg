# Generated by Django 2.2 on 2020-05-20 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log_reg', '0002_comment_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
