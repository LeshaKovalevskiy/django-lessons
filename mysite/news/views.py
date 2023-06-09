from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import News, Category
from .forms import NewsForm
from django.views.generic import ListView


class HomeNews(ListView):
    model = News
    template_name = "news/home_news_list.html"
    context_object_name = "news"
    # extra_context = {"title": "Главная страница"}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        return context

    def get_queryset(self):
        return News.objects.filter(is_published=True)


def index(request):
    news = News.objects.all()
    context = {
        "news": news,
        "title": "Список новостей",
    }
    return render(request, "news/index.html", context=context)


def get_category(request, category_id):
    news = News.objects.filter(category_id=category_id)
    category = Category.objects.get(pk=category_id)
    context = {
        "news": news,
        "category": category,
    }
    return render(request, "news/category.html", context=context)


def view_news(request, news_id):
    # news_item = News.objects.get(pk=news_id)
    news_item = get_object_or_404(News, pk=news_id)
    return render(request, "news/view_news.html", {"news_item": news_item})


def add_news(request):
    if request.method == "POST":
        form = NewsForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data)
            # news = News.objects.create(**form.cleaned_data)
            # return redirect("home")
            news = form.save()
            return redirect(news)
    else:
        form = NewsForm()
    return render(request, "news/add_news.html", context={"form": form})
