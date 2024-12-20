from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


class User(AbstractUser):
    # 为 groups 和 user_permissions 字段指定一个新的 related_name
    groups = models.ManyToManyField(
        Group,
        related_name='%(app_label)s_%(class)s_groups',  # 使用动态 related_name
        blank=True
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='%(app_label)s_%(class)s_user_permissions',  # 使用动态 related_name
        blank=True
    )
