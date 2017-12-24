from django.utils import timezone

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from chan.models import Message, MessageForm


def show_messages(request):
    messages = Message.objects.all()
    context = {'messages' : messages,
               }
    #return HttpResponse("Тут будет лента сообщений")
    return render(request, "chan/show_messages.html", context)


def reply(request, message_id):
    message = Message.objects.get(pk=message_id)
    messages = Message.objects.filter(reply_to_id=message_id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.pub_date = timezone.now()
            new_message.reply_to_id = message_id
            new_message.save()
            return redirect('/chan/reply/%s' %message_id)
    else:
        form = MessageForm()
    context = {'message': message,
               'form': form,
               'messages': messages}
    return render(request, 'chan/reply.html', context)

def new_record(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            new_message = form.save(commit=False)
            new_message.pub_date = timezone.now()
            new_message.save()
            return redirect('/chan/')
    else:
        form = MessageForm()
    return render(request, 'chan/new_record.html', {'form': form})
