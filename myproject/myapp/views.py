from django.shortcuts import render

from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Document, Tag
from .forms import DocumentForm
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.http import JsonResponse
from django.shortcuts import redirect


def cr( request, id):
    try:
        Document.objects.get(id = id).delete()
        response = redirect('list3', id = id)
    except Exception as ex:
        print("Exept")
    return response


def GetP(request,id):
    try:
        #Document.objects.all().delete()
        #Tag.objects.all().delete()
        contact_list = Document.objects.all()
        paginator = Paginator(contact_list, 12)  # Show 25 contacts per page

        documents = paginator.get_page(id)

        # Render list page with the documents and the form
    except Exception as ex:
        print("Exept")
    return render(request, 'list.html', {'documents': documents , 'documents_length':Document.objects.all().count()})


def redirector(request):
    response = redirect('art/1')
    return response


def render_create_post(request):
    try:
        form = DocumentForm()
    except Exception as ex:
        print("Exept")
    return render(request, "add_new_post.html",  {'form': form})


def post_detail(request, title):
    try:
        print(title)
        documents = Document.objects.filter(search_tags__title__in = [title])
    except Exception as ex:
        print("Exept")
    return render(request, "show_by_title.html",context={'documents': documents})


def listing(request,id):
    try:
        print(1)
        contact_list = Document.objects.all()
        paginator = Paginator(contact_list, 5)  # Show 25 contacts per page

        documents = paginator.get_page(id)
    except Exception as ex:
        print("Exept")
    return render(request, 'list111.html', {'documents': documents})


def PostList(request):
    try:
    # Handle file upload
        if request.method == 'POST':

            form = DocumentForm(request.POST, request.FILES)
            print(1)
            if form.is_valid():
                title = request.POST.get('title_').strip() if len(request.POST.get('title_').strip()) != 0 else "default title"
                desciption = request.POST.get('description1').strip()  if len(request.POST.get('description1').strip() ) != 0 else "default description"
                newdoc = Document(docfile=request.FILES['docfile'],
                                  title=  title,
                                  description = desciption )

                newdoc.save()

                if request.POST.get("ggr") != None:
                    for i in request.POST.getlist('ggr'):
                        print(i)

                        tg, created = Tag.objects.get_or_create(title=i)

                        newdoc.search_tags.add(tg)
                        newdoc.save()
                print(2)



                # Render list page with the documents and the form
                #return render(request, 'list.html', {'documents': documents, 'form': form})
                # Redirect to the document list after POST
                return HttpResponseRedirect(reverse('list'))
        else:
            form = DocumentForm() # A empty, unbound form
            print(3)
        print(4)
      #  Document.objects.all().delete()
       # Tag.objects.all().delete()

        print("D "+str(Document.objects.all().count()))
        print("T "+str(Tag.objects.all().count()))


        contact_list = Document.objects.all()
        paginator = Paginator(contact_list, 12)  # Show 25 contacts per page

        documents = paginator.get_page(1)

        # Render list page with the documents and the form
    except Exception as ex:
        print("Exept11")
        print(ex)
    return render(request, 'list.html', {'documents': documents, 'form': form, 'documents_length':Document.objects.all().count()})


def aj(request):
    try:
        if request.method == 'POST':

            form = DocumentForm(request.POST, request.FILES)
            if form.is_valid():

                newdoc = Document(docfile=request.FILES['docfile']
                                  )

                newdoc.save()

                if request.POST.get("ggr") != None:
                    for i in request.POST.getlist('ggr'):
                        print(i)

                        tg, created = Tag.objects.get_or_create(title=i)

                        newdoc.search_tags.add(tg)
                        newdoc.save()
                print(2)

        else:
            form = DocumentForm()  # A empty, unbound form

        documents = Document.objects.all()
        print("fwefw")
        responseData = {
            'id': 4,
            'name': 'Test Response',
            'roles': ['Admin', 'User']
        }
        # Render list page with the documents and the form
    except Exception as ex:
        print("Exept")
    return JsonResponse(responseData)


def create_post(request):
    try:
        documents = Document.objects.all()
    except Exception as ex:
        print("Exept")
    return render(request, 'list.html', {'documents': documents, 'documents_length':Document.objects.all().count()})