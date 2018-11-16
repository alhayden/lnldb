# Generated by Django 2.1.2 on 2018-10-22 01:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import meetings.models


class Migration(migrations.Migration):

    dependencies = [
        ('meetings', '0010_auto_20170323_2350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ccnoticesend',
            name='email_to',
            field=models.ForeignKey(default=meetings.models.get_default_email, on_delete=django.db.models.deletion.PROTECT, to='meetings.TargetEmailList'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='events.Location'),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='meeting_type',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='meetings.MeetingType'),
        ),
        migrations.AlterField(
            model_name='meetingannounce',
            name='email_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='meetings.TargetEmailList'),
        ),
        migrations.AlterField(
            model_name='mtgattachment',
            name='author',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
    ]