from django.apps import AppConfig
from django.db.models.signals import post_migrate


class CompanyConfig(AppConfig):
    name = 'company'

    # migrate時に実行
    def ready(self):
        from default.models import create_default_categories
        post_migrate.connect(create_default_categories, sender=self)
