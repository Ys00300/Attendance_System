from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.views.generic.edit import CreateView
from .models import Message
from .forms import MessageForm
from django.contrib.auth import get_user_model 
from django.views.generic import ListView
from django.views.generic import DetailView
from django.http import Http404

class SendMessageView(CreateView):
    model = Message
    form_class = MessageForm
    template_name = 'send_message.html'

    def form_valid(self, form):
        receiver = get_object_or_404(get_user_model(), id=self.kwargs['receiver_id'])  # Get receiver from URL
        if self.request.user == receiver:
            return HttpResponseForbidden("You cannot send a message to yourself.")

        # Set the sender and receiver
        form.instance.sender = self.request.user
        form.instance.receiver = receiver
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('inbox')  # Redirect to inbox after sending the message


class InboxView(ListView):
    model = Message
    template_name = 'inbox.html'
    context_object_name = 'messages'

    def get_queryset(self):
        # Only fetch messages where the logged-in user is the receiver
        return Message.objects.filter(receiver=self.request.user).order_by('-sent_at')
    
    
class ReadMessageView(DetailView):
    model = Message
    template_name = 'read_message.html'
    context_object_name = 'message'

    def get_object(self):
        # Ensure the message belongs to the logged-in user
        message = super().get_object()
        if message.receiver != self.request.user:
            raise Http404("Message not found.")
        message.mark_as_read()  # Mark the message as read
        return message
