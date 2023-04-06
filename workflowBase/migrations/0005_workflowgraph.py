# Generated by Django 4.1.4 on 2023-04-06 09:48

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('workflowBase', '0004_alter_workflowinstance_history_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WorkflowGraph',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('graph', models.ImageField(blank=True, null=True, upload_to='workflow/')),
                ('workflow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='workflowBase.workflow')),
            ],
            options={
                'verbose_name': 'Workflow Graph',
                'verbose_name_plural': 'Workflow Graphs',
            },
        ),
    ]