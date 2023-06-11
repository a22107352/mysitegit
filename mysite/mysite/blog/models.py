
from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    CATEGORIES = (
        ('tecnologia', 'Tecnologia'),
        ('música', 'Música'),
        ('desporto', 'Desporto'),
        ('no_categorie', 'No Category'),
    )

    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    conteudo = models.TextField()
    data = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)
    descricao = models.TextField(default='')
    categoria = models.CharField(max_length=20, choices=CATEGORIES, default='no_categorie')
    comments = models.ManyToManyField('Comment', related_name='post_comments')

    def __str__(self):
        return self.titulo


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    autor = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    conteudo = models.TextField()

    def __str__(self):
        return f"Comment by {self.autor.username} on {self.post.titulo}"
