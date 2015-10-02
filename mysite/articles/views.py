from django.shortcuts import get_object_or_404, render

from .models import Articles

def index(request):
    latest_articles_list = Articles.objects.all()
    context = {'latest_articles_list': latest_articles_list}
    return render(request, 'articles/index.html', context)
	
def detail(request, articles_id):
    article = get_object_or_404(Articles, pk=articles_id)
    return render(request, 'articles/detail.html', {'article': article})