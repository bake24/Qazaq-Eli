# import requests
# from .forms import CityForm
from django.shortcuts import render, redirect
from .models import City, Contact, Place, Famous, Register
from django.views.generic import DetailView, UpdateView
from .forms import RegisterForm
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect
from django.conf import settings
from django.template import RequestContext




class NewDetailView(DetailView):
    model = Famous
    template_name = 'cityapp/famous.html'
    context_object_name = 'famous_key'


# class NewUpdateView(UpdateView):
#     model = Famous


def index(request):
    return render(request, 'cityapp/index.html')


def city(request):
    # city_info = City.objects.order_by(Length('title'))
    # city_info = City.objects.all()
    return render(request, 'cityapp/city.html')




def contacts(request):
    contact_info = Contact.objects.all()
    return render(request, 'cityapp/contacts.html', {'contact': contact_info})


def places(request):
    place_info = Place.objects.all()
    return render(request, 'cityapp/places.html', {'place': place_info})

def  news(request):
    # news_info = Place.objects.all()
    return render(request, 'cityapp/news.html')


def  history(request):
    history_info = City.objects.all()
    return render(request, 'cityapp/history.html', {'history': history_info})


def  famous(request):
    famous_info = Famous.objects.all()
    return render(request, 'cityapp/famous.html', {'famous': famous_info})

def  create(request):
    err = ''

    if request.method == 'POST':
        form = RegisterForm(request.POST, request.FILES)
        if form.is_valid():
            forma = form.save()

            subject = 'Привет, %s' % forma.name
            message = 'Вы успешно зарегестровались на сайте Qazaq Eli! Следите за новостями.' \
                      ' С вашего счета успешно списано 6990 тенге, по всем вопросам звоните по номеру ' \
                      '+7 747 439 82 79'
            recipient = forma.email
            mail = EmailMessage(
                subject,
                message,
                 'duisenbekov07@gmail.com',
                (recipient,)
            )

            mail.content_subtype = 'html'

            mail.attach_file(forma.image.url)

            mail.send()
            messages.success(request, 'Success!')
            redirect('city')
        else:
            err = 'Form is does not right'

    form = RegisterForm()
    data = {
        'form': form,
        'err': err
    }

    return render(request, 'cityapp/create.html', data)




# def  weather(request):
#     weather_info = Famous.objects.all()
#     return render(request, 'cityapp/weather.html', {'weather': weather_info})
#
# records = ModelName.objects.all()
# records.delete() удаление элементов в модели
#