from django.db import models

class Block(models.Model):
    index = models.PositiveIntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)
    data = models.TextField()
    previous_hash = models.CharField(max_length=64)
    current_hash = models.CharField(max_length=64)

    def __str__(self):
        return f"Block {self.index}"
