# Generated by Django 4.0.7 on 2022-11-09 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('now_app', '0008_alter_nowtimeupdate_lower_buid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nowtimeunitboundaryupdate',
            name='buid',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='nowtimeunitupdate',
            name='tuid',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='refjournal',
            name='journal_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
