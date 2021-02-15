from django.db import models


# Create your models here.
class Server(models.Model):
    server_type_choice = [
        (0, 'PC服务器'),
        (1, '刀片机'),
        (2, '小型机')
    ]
    create_by_choie = [
        ('auto', '自动录入'),
        ('manual', '手动添加')
    ]
    server_type = models.SmallIntegerField(choices=server_type_choice, default=0, verbose_name='服务器类型')
    create_by = models.CharField(max_length=32, choices=create_by_choie, default='auto', verbose_name='添加方式')
    IP = models.CharField(max_length=30, default='', verbose_name='IP地址')

    MAC = models.CharField(max_length=200, default='', verbose_name='MAC地址',null=True,blank=True)
    # :null=True,表示数据库创建时该字段可不填,用NULL填充 :null=True,表示数据库创建时该字段可不填,用NULL填充
    model = models.CharField(max_length=128, null=True, blank=True, verbose_name='服务器型号')
    hostname = models.CharField(max_length=128, null=True, blank=True, verbose_name='主机名')
    os_type = models.CharField(max_length=64, null=True, blank=True, verbose_name='操作系统类型')
    os_distrubiton = models.CharField(max_length=64, null=True, blank=True, verbose_name='发行商')
    os_release = models.CharField(max_length=64, null=True, blank=True, verbose_name='操作系统版本')
    sn = models.CharField(max_length=64, null=True, blank=True, verbose_name='资产标识')

    def __str__(self):
        return self.IP

    class Meta:
        db_table = 'server'
        verbose_name = '服务器管理'
        verbose_name_plural = '服务器管理'


class users(models.Model):
    username = models.CharField(max_length=64, verbose_name='用户名', default='root')
    password = models.CharField(max_length=128, verbose_name='密码', default='123')
    pkey = models.CharField(max_length=128, verbose_name='私钥', default='id_rsa')
    server = models.ForeignKey(Server, on_delete=models.CASCADE, verbose_name='用户所属服务器')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'users'
        verbose_name = '服务器的用户管理'
        verbose_name_plural = '服务器的用户管理'
