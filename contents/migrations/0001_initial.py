# Generated by Django 4.1 on 2023-02-05 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('c_title', models.CharField(max_length=120)),
                ('c_body', models.TextField()),
                ('c_author', models.CharField(max_length=40)),
                ('c_author_updated', models.CharField(max_length=40)),
                ('c_date_created', models.DateField()),
                ('c_date_updated', models.DateField()),
            ],
            options={
                'db_table': 'contents',
            },
        ),
    ]
