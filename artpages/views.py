from django.template.context_processors import request
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse

from .form import NameForm
from django.shortcuts import redirect

from .models import Person, Book
from .form import ContactInfoForm, BookForm


def create_contact_info(request):
    if request.method == 'POST':
        form = ContactInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved Contact info.")
    else:
        form = ContactInfoForm()

    context = {'form': form}

    return render(request, 'home.html', context)


class AboutPageView(TemplateView):  # new
    template_name = "about.html"


def insert_person():
    # query1
    obj1 = Person(first_name="Pradeep", last_name="K", address="Hyderabad")
    obj1.save()


def get_name(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            print('Mons aquiii')

            insert_person()

            value = request.POST.get('your_name')

            if value == 'a':
                value = ''

            print(value, 'risultato del form')

            context = {
                "first_name": value,
            }
            # return response

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return render(request, 'home.html', context)
            # return HttpResponseRedirect('/' % context)

        # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


def create_new_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("New book created")
    else:
        form = BookForm()

    context = {'form': form}

    return render(request, 'newbook.html', context)


def list_of_book(request):
    if request.method == 'GET':
        #all_books = Book.objects.raw("Select * from artpages_book")
        #context = {'all_books': all_books}

        context = {}
        context["dataset"] = Book.objects.all()

        #context["dataset"] = Book.objects.get(id=1)

        return render(request, 'homebook.html', context)

