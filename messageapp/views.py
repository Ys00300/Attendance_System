from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.http import HttpResponse
from .forms import EmailForm



# def send_mail_to_teacher(request):
#         if request.method == 'POST':
#             subject = "I'm on leave!"
#             message = "This is a test message"
#             from_email = settings.EMAIL_HOST_USER
#             recipient_list = ['yashswami00300@gmail.com']  # spelling fix here

#             send_mail(subject, message, from_email, recipient_list)
#             return redirect('/')  # specify a URL or a named URL pattern
#         return redirect('/')

class SendEmailView(FormView):
    template_name = 'send_message.html'
    form_class = EmailForm
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        subject = form.cleaned_data['subject']
        from_email = settings.EMAIL_HOST_USER
        message = form.cleaned_data['message']
        recipient = form.cleaned_data['recipient']
      

        try:
            send_mail(subject,message,from_email,[recipient])
            return super().form_valid(form)
        except Exception as e:
            return HttpResponse(f'Failed to send email :{e}')
