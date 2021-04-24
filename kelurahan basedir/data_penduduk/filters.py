import django_filters
from django_filters import DateFilter,CharFilter

from .models import *

class PendudukFilter(django_filters.FilterSet):
    note = CharFilter(field_name="nama", lookup_expr='icontains')

    class Meta:
        model = Penduduk
        fields = ''