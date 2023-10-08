from django.urls import path

from . import views

app_name = 'quotes_app'

urlpatterns = [
    path('', views.main, name='main'),
    path('scrape/', views.scrape_quotes, name='scrape'),
    path('tag/<str:tag_name>/', views.tag, name='tag'),
    path('author/<str:author_name>/', views.author_info, name='author'),
    path('add/author/', views.add_author, name='author_form'),
    path('add/quote/', views.add_quote, name='quote_form'),
]
