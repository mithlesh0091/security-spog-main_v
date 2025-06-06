# Generated by Django 5.2.1 on 2025-05-23 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AutotaskTicket',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('ticket_number', models.CharField(max_length=255)),
                ('title', models.TextField()),
                ('description', models.TextField()),
                ('status', models.CharField(max_length=50)),
                ('priority', models.IntegerField()),
                ('company_id', models.BigIntegerField()),
                ('contact_id', models.BigIntegerField()),
                ('assigned_resource_id', models.BigIntegerField()),
                ('create_date', models.DateTimeField()),
                ('last_activity_date', models.DateTimeField()),
                ('resolved_date', models.DateTimeField(null=True)),
                ('due_date', models.DateTimeField(null=True)),
                ('resolution', models.TextField(null=True)),
            ],
            options={
                'db_table': 'autotask_tickets',
                'managed': False,
            },
        ),
    ]
