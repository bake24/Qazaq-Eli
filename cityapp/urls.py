from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'main'),
    path('city', views.city, name = 'city'),
    path('contacts', views.contacts, name = 'contacts'),
    path('places', views.places, name = 'places'),
    path('news', views.news, name = 'news'),
    path('history', views.history, name = 'history'),
    path('famous', views.famous, name = 'famous'),
    path('<int:pk>', views.NewDetailView.as_view(), name = 'news-detail'),
    path('create', views.create, name = 'create'),

    # path('<int:pk>/update', views.NewUpdateDetailView.as_view(), name = 'news-update')

    # path('admin/', admin.site.urls),
    # path('', include('weather.urls')),





]
