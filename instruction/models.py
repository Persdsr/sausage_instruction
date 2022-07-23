from ckeditor.fields import RichTextField
from django.db import models
from django.urls import reverse

from mptt.models import MPTTModel, TreeForeignKey


class Post(MPTTModel):
    title = models.CharField(max_length=100)
    description = RichTextField()
    parent = TreeForeignKey('self',
                            related_name='children',
                            on_delete=models.CASCADE,
                            null=True,
                            blank=True)
    slug = models.SlugField(unique=True, max_length=150)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'instr': self.slug})

    def __str__(self):
        return self.title

    class MPTTMeta:
        order_insertion_by = ['title']

    '''ДЛЯ КАЖДОГО ШАГА СДЕЛАТЬ IMAGE ШАГ --> НОВЫЙ КЛАСС ШАЖЕЧЕК С INLINE В АДМИНКЕ '''

    '''POST --> INSTRUCTION (TITLE DISCRIPTION(BLANK=TRUE) >> STEPS(TEXT IMAGE(BLANK=TRUE)'''


class Step(models.Model):
    title = models.CharField(max_length=100)
    text = RichTextField()
    image = models.ImageField(upload_to='steps/', blank=True)
    post = models.ForeignKey(Post, on_delete=models.SET_NULL, null=True,related_name='step_post')

    def __str__(self):
        return self.title









