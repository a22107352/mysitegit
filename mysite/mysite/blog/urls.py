from django.contrib import admin
from django.urls import path
from .views import (
    blog_view,
    criar_post,
    like_post,
    remover_post,
    create_comment,
    delete_comment,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', blog_view, name='blog_view'),
    path('post/create/', criar_post, name='criar_post'),
    path('post/<int:post_id>/like/', like_post, name='like_post'),
    path('post/<int:post_id>/remover/', remover_post, name='remover_post'),
    path('post/<int:post_id>/comment/', create_comment, name='create_comment'),
path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]
