from django.urls import path
from .views import news_list, news_detail, homeView, ContactPageView, aboutusPageView, categoryPageView

urlpatterns = [
    path('', homeView, name='home_page'),
    path('news/', news_list, name="all_news_list"),
    path('news/<int:id>/', news_detail, name="news_detail_page"),
    path('contact/', ContactPageView.as_view(), name='contact_page'),
    path('about-us/', aboutusPageView, name='aboutus_page'),
    path('category/', categoryPageView, name='category_page')
]