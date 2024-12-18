import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):
    user_nickname = django_filters.CharFilter(field_name='user_id__nickname', lookup_expr='icontains')
    date = django_filters.DateFromToRangeFilter()

    class Meta:
        model = Post
        fields = ['user_nickname', 'date']