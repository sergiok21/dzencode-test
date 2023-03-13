from django.db import models


class Comments(models.Model):
    name = models.CharField(max_length=256)
    email = models.EmailField(max_length=256)
    home_page = models.URLField(max_length=256, blank=True, null=True)
    message = models.TextField()
    parent_comment = models.IntegerField(blank=True, null=True)
    created_timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-id']
