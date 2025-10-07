from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Category(models.Model):
    slug = models.SlugField(max_length=120, unique=True)
    name = models.CharField(max_length=100, verbose_name="Назва")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категорія"
        verbose_name_plural = "Категорії"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Post(models.Model):
    slug = models.SlugField(max_length=220, unique=True, db_index=True)
    title = models.CharField(max_length=200, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Опис")
    published_date = models.DateTimeField(auto_created=True, verbose_name="Дата публікації")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Категорія")
    auther = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор", default=1)
    image = models.URLField(
        default="https://soliloquywp.com/wp-content/uploads/2016/08/How-to-Set-a-Default-Featured-Image-in-WordPress.png")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Публікація"
        verbose_name_plural = "Публікації"
