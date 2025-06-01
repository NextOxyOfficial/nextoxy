from django.db import models

# Create your models here.
class BlockGroup(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class BlockCategory(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Block(models.Model):
    name = models.CharField(max_length=200)
    group = models.ForeignKey(BlockGroup, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(BlockCategory, on_delete=models.SET_NULL, null=True, blank=True)
    content = models.JSONField(null=True, blank=True)
    html = models.TextField(null=True, blank=True)
    dj = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.name