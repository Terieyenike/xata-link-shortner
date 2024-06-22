from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from xata.client import XataClient

from .models import Link
from .forms import LinkForm

xata = XataClient()


# Create your views here.
def index(request):
    links = xata.data().query("links_link", {
        "columns": [
            "xata_id",
            "clicks",
            "id",
            "name",
            "slug",
            "url"
        ],
        "sort": {"name": "desc"}
    })
    context = {
        "links": links['records']
    }
    return render(request, 'links/index.html', context)


def root_link(request, link_slug):
    link = get_object_or_404(Link, slug=link_slug)
    link.click()
    return redirect(link.url)


def add_link(request):
    if request.method == "POST":
        form = LinkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse("home"))
    else:
        form = LinkForm
    context = {
        "form": form
    }
    return render(request, "links/create.html", context)
