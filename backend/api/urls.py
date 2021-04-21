from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import search_stocks_by_name

urlpatterns = {
    path('', search_stocks_by_name, name="search_stock_by_name"),
    # path('<slug:key>', manage_item, name="single_item")
}
urlpatterns = format_suffix_patterns(urlpatterns)
