from django.urls import path
from .views import news_list, news_detail, homeView

urlpatterns = [
    path('', homeView, name='home_page'),
    path('all/', news_list, name="all_news_list"),
    path('<int:id>/', news_detail, name="news_detail_page"),
]