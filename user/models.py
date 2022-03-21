import random

from django.db import models

# Create your models here.

def default_sign():
    sign_list = ['向前冲','希望我们相遇','加入我们','不要后悔','希望不灭']
    return random.choice(sign_list)



class UserProfile(models.Model):

    username = models.CharField(verbose_name='用户名', max_length=11,primary_key=True)
    nickname = models.CharField(verbose_name='昵称', max_length=30)
    email = models.EmailField(verbose_name='邮箱',max_length=50)
    phone = models.CharField(verbose_name='手机号',max_length=11)
    password = models.CharField(verbose_name='密码',max_length=32)
    sign = models.CharField (verbose_name='个人签名', max_length=50,default=default_sign)
    info = models.CharField(verbose_name='个人描述', max_length=150,default='')
    avatar = models.ImageField(verbose_name='头像', upload_to='avatar', null=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(auto_now=True)


    class Meta:
        db_table = 'user_user_profile'
