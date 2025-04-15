from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings
from django.urls import reverse_lazy
from django.views.generic.edit import FormView
from .forms import EmailForm
from .models import Teacher  # Make sure you import Teacher model if needed

class SendEmailView(FormView):
    template_name = 'send_message.html'
    form_class = EmailForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # Retrieve form data
        from_date = form.cleaned_data['from_date']
        to_date = form.cleaned_data['to_date']
        cc_teacher = form.cleaned_data['cc_teacher']
        reason = form.cleaned_data['reason']
        recipient_type = form.cleaned_data['recipient_type']        
        
        
        
        
        
        
        
        
        
        

        # # Prepare the message body
        # message = f"From: {from_date}\nTo: {to_date}\nReason: {reason}"
        # # breakpoint()
        # # Prepare the list of recipients
        # recipients = []

        # # Check recipient_type to determine who will get the email
        # if recipient_type == 'student':
        #     recipients.append(self.request.user.email)  # Sending email to the student (logged-in user)
        # elif recipient_type == 'teacher':
        #     teacher = Teacher.objects.filter(user=self.request.user).first()
        #     if teacher:
        #         recipients.append(teacher.user.email)  # Sending email to the teacher
        #     else:
        #         return HttpResponse('Teacher not found for this user.')

        # # Additionally, send email to the other party (teacher if sending to student or student if sending to teacher)
        # if recipient_type == 'student':
        #     teacher = Teacher.objects.filter(user=self.request.user).first()
        #     if teacher:
        #         recipients.append(teacher.user.email)  # Send email to the teacher as well

        # if recipient_type == 'teacher':
        #     # If the recipient type is teacher, add the student email as well
        #     recipients.append(

        # # Prepare CC list (if provided)
        # cc_list = []
        # if cc_teacher:
        #     cc_list.append(cc_teacher)  # Add CC teacher if provided

        # # Send the email
        # from_email = settings.EMAIL_HOST_USER
        # subject = "Leave Notification"  # You can customize the subject as needed
        
        # try:
            
        #     send_mail(subject, message, from_email, ['swamidanish00100@gmail.com'], fail_silently=False)
            
        #     return super().form_valid(form)
        # except Exception as e:
        #     return HttpResponse(f'Failed to send email: {e}')
