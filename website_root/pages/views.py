from django.shortcuts import render, get_object_or_404
from .models import Page

def render_pages(request, pagename):
    permalink = "".join(["/", pagename])
    page = get_object_or_404(Page, permalink=permalink)
    context = {
        "title": page.title,
        "content": page.page_content,
        "page_list": Page.objects.all()
    }
    return render(request, 'pages/page.html', context)
