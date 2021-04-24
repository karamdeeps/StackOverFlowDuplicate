from django.db import models


class Question(models.Model):
    question = models.CharField(max_length=200, null=True, blank=True)
    vote_count = models.IntegerField(default=0)
    views      = models.CharField(max_length=100)
    tags       = models.CharField(max_length=250)

    def __str__(self):
        return "%s" % self.question
