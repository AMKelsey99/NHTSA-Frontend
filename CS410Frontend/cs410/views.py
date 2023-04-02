from django.shortcuts import render
# from .forms import placeholderform
from .models import placeholder


def main(request):
    context = {'placeholder_table':placeholder.objects.all()}
    return render(request, 'main.html', context)

def search(request):
    model = placeholder;
    query = request.GET.get("searchterm") or ''
    placeholdersearch = placeholder.objects.filter(field1__contains=query) or placeholder.objects.filter(field2__contains=query) or placeholder.objects.filter(field3__contains=query)
    context = {"placeholdersearch": placeholdersearch}
    return render(request, 'main.html', context)
