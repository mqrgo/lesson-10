from django.db import models
from django.urls import reverse
from slugify import slugify


class Department(models.Model):
    title = models.CharField(max_length=150, verbose_name='Отдел')
    slug = models.SlugField(verbose_name='Слаг', editable=False)

    class Meta:
        ordering = ['title']
        verbose_name = 'Отдел'
        verbose_name_plural = 'Отделы'

    def __str__(self):
        return self.title

    def save(self, *ar, **kw):
        self.slug = slugify(self.title)
        super().save(*ar, **kw)


class Journalist(models.Model):
    first_name = models.CharField(max_length=50, verbose_name='Имя')
    last_name = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='Дата рождения')
    department = models.ForeignKey(
        Department,
        on_delete=models.SET_DEFAULT,
        default='Без отдела',
        related_name='journalist'
    )
    photo = models.ImageField(
        upload_to='images/',
        verbose_name='Фото',
        null=True,
        blank=True
    )
    is_married = models.BooleanField(default=False, verbose_name='В браке')
    salary = models.SmallIntegerField(verbose_name='Зарплата')

    class Meta:
        ordering = ['first_name', 'last_name']
        verbose_name = 'Журналист'
        verbose_name_plural = 'Журналисты'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_absolute_url(self):
        return reverse("model_detail",
                       args=[
                           self.first_name,
                           self.last_name,
                           self.birthday.year,
                           self.birthday.month,
                           self.birthday.day
                       ])
