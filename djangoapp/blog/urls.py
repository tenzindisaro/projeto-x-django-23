from django.urls import path
from blog.views import PostListView, page, post, CreatedByListView, CategoryListViwe, TagListViwe, SearchListViwe

app_name = 'blog'

urlpatterns = [
    path('', PostListView.as_view(), name='index'),
    path('page/<slug:slug>/', page, name='page'),
    path('post/<slug:slug>/', post, name='post'),
    path('created_by/<int:author_pk>/', CreatedByListView.as_view(), name='created_by'),
    path('category/<slug:slug>/', CategoryListViwe, name='category'),
    path('tag/<slug:slug>/', TagListViwe, name='tag'),
    path('search/', SearchListViwe, name='search'),
]

