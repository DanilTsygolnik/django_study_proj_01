from django.shortcuts import render, get_object_or_404
from . models import Page

def index(request, pagename):
    slash_pagename = ''.join(['/', pagename])
    page = get_object_or_404(Page, permalink=slash_pagename)
    context = {
        'title': page.title,
        'content': page.body_html,
        'page_list': Page.objects.all(),
        #'pages_list_for_nav': Page.objects.all(),
    }
    # assert False
    return render(request, 'pages/page.html', context)
