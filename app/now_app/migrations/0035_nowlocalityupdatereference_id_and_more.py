# Generated by Django 4.0.7 on 2022-10-31 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0034_alter_nowlocalityupdate_lid'),
    ]

    operations = [
        migrations.AddField(
            model_name='nowlocalityupdatereference',
            name='id',
            field=models.BigAutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='nowlocalityupdatereference',
            name='luid',
            field=models.OneToOneField(db_column='luid', on_delete=django.db.models.deletion.DO_NOTHING, to='now_app.nowlocalityupdate'),
        ),
    ]