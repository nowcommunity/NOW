# Generated by Django 4.0.7 on 2022-10-31 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0052_nowstratcoordpeople_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nowlocalitysynonym',
            name='lid',
            field=models.ForeignKey(db_column='lid', on_delete=django.db.models.deletion.CASCADE, to='now_app.nowlocality'),
        ),
    ]
