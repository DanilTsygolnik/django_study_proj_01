from django.shortcuts import render, get_object_or_404
from .models import Page
from .forms import ContactForm

def render_pages(request, pagename):
    permalink = "".join(["/", pagename])
    page = get_object_or_404(Page, permalink=permalink)
    context = {
        "title": page.title,
        "content": page.page_content,
        "page_list": Page.objects.all()
    }
    return render(request, 'pages/page.html', context)

def render_contact_form(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            return render(request, 'contact/form_sent.html', {'page_list': Page.objects.all()})
    form = ContactForm()
    return render(request, 'contact/contact.html', {'form': form, 'page_list': Page.objects.all()})
