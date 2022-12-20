import django_tables2 as tables
from .models import Exprecord

class SimpleTable(tables.Table):
    class Meta:
        model = Exprecord
        template_name = "django_tables2/bootstrap-responsive.html"
        exclude = ['id']