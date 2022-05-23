from django.urls import path
from . import views
from .views import CustomLoginView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('', views.index, name = 'main'),
    path('city', views.city, name = 'city'),
    path('contacts', views.contacts, name = 'contacts'),
    path('places', views.places, name = 'places'),
    path('news', views.news, name = 'news'),
    path('history', views.history, name = 'history'),
    path('famous', views.famous, name = 'famous'),
    path('<int:pk>', views.NewDetailView.as_view(), name = 'news-detail'),
    path('create', views.create, name = 'create'),
    path('all_places', views.all_places, name = 'all_places'),
    path('all_famous', views.all_famous, name = 'all_famous'),

    # path('<int:pk>/update', views.NewUpdateDetailView.as_view(), name = 'news-update')

    # path('admin/', admin.site.urls),
    # path('', include('weather.urls')),





]
