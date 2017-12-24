from django.db import models

# Create your models here.
from django.forms import ModelForm


class Message(models.Model):
    text_mess = models.TextField()
    pub_date = models.DateField()
    reply_to = models.ForeignKey("Message", null = True)

    def __str__(self):
        return self.text_mess


class MessageForm(ModelForm):
    class Meta:
        model = Message
        exclude = ['pub_date', 'reply_to']