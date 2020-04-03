# Generated by Django 3.0.5 on 2020-04-03 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssociatedPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='RelationshipTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15, unique=True)),
                ('description', models.CharField(max_length=25)),
                ('image', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('Date', models.DateField()),
                ('amount', models.IntegerField()),
                ('associatedPerson', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personalfinance.AssociatedPerson')),
                ('tags', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personalfinance.Tags')),
            ],
        ),
        migrations.AddField(
            model_name='associatedperson',
            name='relationship_tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='personalfinance.RelationshipTag'),
        ),
    ]