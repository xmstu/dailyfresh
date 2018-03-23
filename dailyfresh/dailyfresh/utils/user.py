from django.contrib.auth.models import AbstractUser
from .models import BaseModel


class User(BaseModel, AbstractUser):
    """用户信息模型类"""

    class Meta:
        db_table = 'df_user'