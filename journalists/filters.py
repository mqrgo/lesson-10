import django_filters
from journalists.models import Journalist as JR
from django.db.models import Q


class Journalist(django_filters.FilterSet):
    first_name = django_filters.CharFilter(
        label='Имя',
        lookup_expr='icontains',
    )

    last_name = django_filters.CharFilter(
        label='Фамилия',
        lookup_expr='icontains',
    )

    salary_lower = django_filters.NumberFilter(
        field_name='salary',
        label='Заплата ниже чем',
        lookup_expr='lt',
    )

    fi = django_filters.CharFilter(
        method='fi_filter',
        label='Фамилия Имя',
    )

    class Meta:
        model = JR
        exclude = ('photo')

    def fi_filter(self, queryset, name, value):
        return queryset.filter(
            Q(first_name__icontains=value) | Q(last_name__icontains=value)
        )
