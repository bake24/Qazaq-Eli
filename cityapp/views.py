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
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from .forms import UserUpdateForm, ProfileUpdateForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from .models import Profile


class CustomLoginView(LoginView):
    template_name = 'cityapp/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('main')


class RegisterPage(FormView):
    template_name = 'cityapp/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('main')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('main')
        return super(RegisterPage, self).get(*args, **kwargs)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'cityapp/register.html', {'form': form})


@login_required(login_url="/login/")
def profile(request):
    Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'cityapp/profile.html', context)




class NewDetailView(DetailView):
    model = Famous
    template_name = 'cityapp/famous.html'
    context_object_name = 'famous_key'


# class NewUpdateView(UpdateView):
#     model = Famous

@login_required(login_url="/login/")
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

def  all_places(request):
    # news_info = Place.objects.all()
    return render(request, 'cityapp/all_places.html')


def  all_famous(request):
    # news_info = Place.objects.all()
    return render(request, 'cityapp/all_famous.html')



# def  weather(request):
#     weather_info = Famous.objects.all()
#     return render(request, 'cityapp/weather.html', {'weather': weather_info})
#
# records = ModelName.objects.all()
# records.delete() удаление элементов в модели
#