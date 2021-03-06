from django.db import models
from django.conf import settings
from django.template.defaultfilters import slugify
from django.urls import reverse
import uuid


# Create your models here.
class Condition(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Condition, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Color, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Size(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Size, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    image = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(SubCategory, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    class Meta:
        ordering = ["-ordering"]

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Tag, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Article(models.Model):
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, related_name="articles",
                                 default="a68d46c1-4f68-4646-ba66-0081204e17a0")
    subcategory = models.ForeignKey(SubCategory, related_name="articles",
                                    on_delete=models.DO_NOTHING, blank=True, null=True,
                                    default="45f33c1c-4e69-483d-bdc8-7337327c441b")
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    price = models.PositiveIntegerField()
    condition = models.ForeignKey(Condition, on_delete=models.DO_NOTHING, related_name="articles")
    tag = models.ManyToManyField(Tag, related_name="articles", blank=True)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, related_name="articles", blank=True,
                              default='69bfb95a-6732-4047-9553-b20b530a86b4')
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING, related_name="articles", blank=True,
                             default='9d95b2a1-de4f-478f-9037-eb4f6058dfb1')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    change = models.BooleanField(default=False)
    give = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    premium = models.BooleanField(default=False)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(editable=False)
    ordering = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Article, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("article-detail", kwargs={"pk": self.pk})

    def get_absolute_url_user(self):
        return reverse("article-user", kwargs={"pk": self.pk})

    def get_delete_url(self):
        return reverse("article-delete", kwargs={"pk": self.pk})

    def get_update_url(self):
        return reverse("article-update", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
