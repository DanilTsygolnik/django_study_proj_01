from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView

from .forms import QuoteForm
from .models import Quote
from pages.models import Page

class QuoteList(ListView):
    model = Quote
    context_object_name = 'all_quotes'

def quote_req(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/quote/?submitted=True')
    form = QuoteForm()
    if 'submitted' in request.GET:
        submitted = True
    return render(request, 'quotes/quote.html', {'form': form, 'page_list': Page.objects.all(), 'submitted': submitted})

