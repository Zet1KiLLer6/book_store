from django.contrib.auth import get_user_model
from django.db import models

User  = get_user_model()

class Book(models.Model):
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="posts", verbose_name="Владелец книги"
    )
    title = models.CharField("Название", max_length=70)
    description = models.TextField("Описание", blank=True, null=True)
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)
    updated_at = models.DateTimeField("Дата обновления", auto_now=True)

    def __str__(self):
        return f"{self.title}"