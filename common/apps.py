from django.apps import AppConfig


class CommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'common'
    '''
    当 Django 项目启动时，它会依次检查INSTALLED_APPS列表中的每一个条目。
    当它遇到'common.apps.CommonConfig'时，会根据这个条目去查找common应用的相关信息。
    具体来说，它会找到common/apps.py文件中的CommonConfig类，并实例化这个类。
    通过这个类，Django 可以了解到common应用的具体配置，包括它的模块路径等重要信息
    '''
