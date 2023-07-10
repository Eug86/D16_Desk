import django_filters
from django_filters import FilterSet, ModelChoiceFilter
from django.forms import DateTimeInput


class AnnFilter(FilterSet):
    title = django_filters.CharFilter(
        field_name='title',
        lookup_expr='icontains',
        label='Title',
    )
    dateCreation = django_filters.DateTimeFilter(
        field_name='time_in',
        lookup_expr='gt',
        label='Date',
        widget=DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
