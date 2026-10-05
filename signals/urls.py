from django.urls import path
from .views import news_list, news_detail, homeView, ContactPageView, aboutusPageView, categoryPageView, HomePageView, \
WorldPageView, TechPageView, EconPageView, EduPageView, SportsPageView, FinancePageView

urlpatterns = [
    path('', homeView, name='home_page'),
    path('news/', news_list, name="all_news_list"),
    path('news/<slug:news>/', news_detail, name="news_detail_page"),
    path('contact/', ContactPageView.as_view(), name='contact_page'),
    path('about-us/', aboutusPageView, name='aboutus_page'),
    path('category/', categoryPageView, name='category_page'),
    path('world/', WorldPageView.as_view(), name='world_news_page'),
    path('technology/', TechPageView.as_view(), name='tech_news_page'),
    path('economics/', EconPageView.as_view(), name='econ_news_page'),
    path('education/', EduPageView.as_view(), name='edu_news_page'),
    path('sports/', SportsPageView.as_view(), name='sports_news_page'),
    path('finance/', FinancePageView.as_view(), name='finance_news_page'),
]