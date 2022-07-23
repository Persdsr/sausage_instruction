from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import *


class StepInline(admin.StackedInline):
    model = Step
    extra = 1


@admin.register(Post)
class PostAdmin(MPTTModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    save_on_top = True
    inlines = [StepInline]



admin.site.register(Step)



