from django.urls import path
from .views import news_list, news_detail, homeView, contactPageView

urlpatterns = [
    path('', homeView, name='home_page'),
    path('news/', news_list, name="all_news_list"),
    path('news/<int:id>/', news_detail, name="news_detail_page"),
    path('contact/', contactPageView, name='contact_page'),
]