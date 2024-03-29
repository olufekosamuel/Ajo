# Generated by Django 2.2.2 on 2019-08-12 11:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_remove_ajogroup_group_member'),
    ]

    operations = [
        migrations.CreateModel(
            name='AjoMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.AjoGroup')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='participant', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
