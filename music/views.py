from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
# from django.template import loader
from .models import Album


# Create your views here.
def index(request):
    all_albums = Album.objects.all()

    # before loader
    # html = ''
    # for album in all_albums:
    #     url = "/music/" + str(album.id) + "/"
    #     html += '<a href="' + url + '">' + album.album_title + '</a><br/>'

    # for loader
    # template = loader.get_template('music/index.html')
    # return HttpResponse(template.render(context, request))

    return render(request, "music/index.html", {"all_albums": all_albums})


def detail(request, album_id):
    try:
        album = Album.objects.get(pk=album_id)
    except Album.DoesNotExist:
        raise Http404("Sorry, Album does not exists.")
    return render(request, "music/detail.html", {'album':album})