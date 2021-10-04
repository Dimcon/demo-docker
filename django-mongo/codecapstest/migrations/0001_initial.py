# Generated by Django 3.0.5 on 2021-05-06 10:38

from django.db import migrations, models
import djongo.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testModel',
            fields=[
                ('id', djongo.models.fields.GenericObjectIdField(db_column='_id', primary_key=True, serialize=False)),
                ('testField', models.CharField(max_length=50)),
                ('testField2', models.DecimalField(decimal_places=5, default=0, max_digits=20)),
            ],
        ),
    ]
