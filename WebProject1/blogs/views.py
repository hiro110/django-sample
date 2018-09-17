#from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings

from azure.storage.blob import BlockBlobService

@login_required
def index(request):

    service = BlockBlobService(account_name=settings.AZURE_ACCOUNT_NAME,account_key=settings.AZURE_ACCOUNT_KEY)
    context = {'objects' : service.list_blobs(settings.AZURE_CONTAINER)}
    return render(request, 'registration/index.html', context)

@login_required
def detail(request, pk):
    return HttpResponse("Post %s" % pk)

@login_required
def create(request):
    return HttpResponse("Add New Post")

@login_required
def update(request, pk):
    return HttpResponse("Edit Post %s" % pk)

@login_required
def delete(request, pk):
    return HttpResponse("Delete Post %s" % pk)