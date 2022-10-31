# Generated by Django 4.0.7 on 2022-10-31 17:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0043_nowprojectspecies_id_alter_nowprojectspecies_pid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nowregcoordcountry',
            name='reg_coord',
            field=models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='now_app.nowregcoord'),
        ),
        migrations.AddField(
            model_name='nowregcoordcountry',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]