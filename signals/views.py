from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News, Category
from .forms import ContactForm
from django.views.generic import TemplateView



# Create your views here.
def news_list(request):
    # news_list = News.objects.filter(status=News.Status.Published)
    news_list = News.published.all()
    context = {
        "news_list": news_list
    }
    return render(request, "news/news_list.html", context)



def news_detail(request, id):
    news = get_object_or_404(News, id=id, status=News.Status.Published)
    context = {
        "news":news
    }
    return render(request, 'news/news_detail.html', context)



def homeView(request):
    news_list = News.published.all().order_by('-publish_time')[:10]
    categories = Category.objects.all()
    world_news = News.published.all().filter(category__name="World")
    context = {
        'news_list': news_list,
        "categories": categories,
        "world_news": world_news,
    }

    return render(request, 'news/home.html', context)


# def contactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST" and form.is_valid():
#         form.save()
#         return HttpResponse("<h2> Thanks for contacting us!")
#     context = {
#         "form": form
#     }
#     return render(request, 'news/contact.html', context)



class ContactPageView(TemplateView):
    template_name = 'news/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'news/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Thanks for contacting us!</h2>")

        context = {
            "form": form
        }

        return render(request, 'news/contact.html', context)




def categoryPageView(request):
    context = {

    }
    return render(request, 'news/catagory.html', context)








def aboutusPageView(request):
    context = {

    }
    return render(request, 'news/about-us.html', context)