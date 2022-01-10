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
                                    on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=400)
    price = models.PositiveIntegerField()
    condition = models.ForeignKey(Condition, on_delete=models.DO_NOTHING, related_name="articles")
    tag = models.ManyToManyField(Tag, related_name="articles", blank=True)
    color = models.ForeignKey(Color, on_delete=models.DO_NOTHING, related_name="articles", blank=True,
                              default='18fc9abc-2459-4551-b34a-0ae89181417b')
    size = models.ForeignKey(Size, on_delete=models.DO_NOTHING, related_name="articles", blank=True,
                             default='f816d8bb-3c3c-457f-b74c-ec4fa68aeb81')
    photo_main = models.ImageField(upload_to='photos/%Y/%m/')
    photo_1 = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    photo_2 = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    photo_3 = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    photo_4 = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    photo_5 = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
    photo_6 = models.ImageField(upload_to='photos/%Y/%m/', blank=True, null=True)
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
