# Generated by Django 4.0.7 on 2022-10-31 17:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0057_nowtimeunitboundaryreference_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nowtimeunitupdatereference',
            name='tuid',
            field=models.OneToOneField(db_column='tuid', on_delete=django.db.models.deletion.CASCADE, to='now_app.nowtimeunitupdate'),
        ),
    ]
