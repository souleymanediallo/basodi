# Generated by Django 4.0 on 2022-01-07 16:42

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/')),
                ('description', models.TextField(blank=True, null=True)),
                ('ordering', models.IntegerField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('ordering', models.IntegerField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['-ordering'],
            },
        ),
        migrations.CreateModel(
            name='Condition',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('ordering', models.IntegerField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['-ordering'],
            },
        ),
        migrations.CreateModel(
            name='Size',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('ordering', models.IntegerField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['-ordering'],
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('image', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/')),
                ('description', models.TextField(blank=True, null=True)),
                ('ordering', models.IntegerField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['-ordering'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField(editable=False)),
                ('ordering', models.IntegerField(default=0)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
            options={
                'ordering': ['-ordering'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=400)),
                ('price', models.PositiveIntegerField()),
                ('photo_main', models.ImageField(upload_to='photos/%Y/%m/')),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/')),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/')),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/')),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/')),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/')),
                ('photo_6', models.ImageField(blank=True, null=True, upload_to='photos/%Y/%m/')),
                ('give', models.BooleanField(default=False)),
                ('published', models.BooleanField(default=True)),
                ('premium', models.BooleanField(default=False)),
                ('slug', models.SlugField(editable=False)),
                ('ordering', models.IntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customuser')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='articles', to='articles.category')),
                ('color', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='articles', to='articles.color')),
                ('condition', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='articles', to='articles.condition')),
                ('size', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='articles', to='articles.size')),
                ('subcategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='articles', to='articles.subcategory')),
                ('tag', models.ManyToManyField(blank=True, related_name='articles', to='articles.Tag')),
            ],
        ),
    ]
