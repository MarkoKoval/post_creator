from django.shortcuts import render


from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Document, Tag
from .forms import DocumentForm
from django.core.paginator import Paginator
from django.shortcuts import redirect


def delete_post_by_id( request, id):
    try:
        Document.objects.get(id = id).delete()
        response = redirect('get_posts_by_paginator', id = 1)
    except Exception as ex:
        print("Exept")
    return response


def get_posts_by_paginator(request,id):
    try:
        #Document.objects.all().delete()
        #Tag.objects.all().delete()
        contact_list = Document.objects.all()
        paginator = Paginator(contact_list, 12)  # Show 25 contacts per page

        documents = paginator.get_page(id)
    except Exception as ex:
        print("Exept")
    return render(request, 'list.html', {'documents': documents , 'documents_length':Document.objects.all().count()})


def get_posts_by_paginator_redirector(request):
    response = redirect('page/1')
    return response


def create_new_post(request):
    try:
        form = DocumentForm()
    except Exception as ex:
        print("Exept ")
    return render(request, "add_new_post.html",  {'form': form})


def get_posts_by_tags(request, title):
    try:
        print(title)
        documents = Document.objects.filter(search_tags__title__in = [title])
    except Exception as ex:
        print("Exept")
    return render(request, "show_by_title.html",context={'documents': documents})


def handle_form(request):
    try:
    # Handle file upload
        if request.method == 'POST':

            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():
                title = request.POST.get('title_').strip() if len(request.POST.get('title_').strip()) != 0 else "default title"
                desciption = request.POST.get('description1').strip()  if len(request.POST.get('description1').strip() ) != 0 else "default description"
                newdoc = Document(docfile=request.FILES['docfile'],
                                  title=title,
                                  description=desciption)

                newdoc.save()

                if request.POST.get("search_tags"):
                    for i in request.POST.getlist('search_tags'):
                        print(i)

                        tg, created = Tag.objects.get_or_create(title=i)

                        newdoc.search_tags.add(tg)
                        newdoc.save()

                return HttpResponseRedirect(reverse('list'))
        else:
            form = DocumentForm() # A empty, unbound form
        contact_list = Document.objects.all()
        paginator = Paginator(contact_list, 12)  # Show 25 contacts per page

        documents = paginator.get_page(1)

        # Render list page with the documents and the form
    except Exception as ex:
        print("Exept11")
        print(ex)
    response = redirect('page/1')
    return response

