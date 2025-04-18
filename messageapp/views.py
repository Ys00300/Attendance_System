# views.py
from django.views.generic.edit import FormView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
from django.urls import reverse_lazy
from .forms import EmailForm
from .models import Teacher, Message


@method_decorator(login_required, name='dispatch')
class SendEmailView(FormView):
    template_name = 'send_message.html'
    form_class = EmailForm
    success_url = reverse_lazy('home') # redirect back or change as needed

    def dispatch(self, request, *args, **kwargs):
        if not hasattr(request.user, 'student'):
            messages.error(request, "Only students can send emails to teachers.")
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        student_user = self.request.user
        reason = form.cleaned_data['reason']
        cc_email = form.cleaned_data['cc_teacher']
        from_date = form.cleaned_data['from_date']
        to_date = form.cleaned_data['to_date']

      
        teacher = Teacher.objects.first()
        if not teacher:
            messages.error(self.request, "No teacher available to receive the email.")
            return self.form_invalid(form)

        # Email content
        subject = "Leave Request from Student"
        email_message = f"""
        Leave Request

        From: {student_user.get_full_name()} ({student_user.email})
        Date Range: {from_date} to {to_date}
        Reason: {reason}
        """

        recipients = [teacher.user.email]
        if cc_email:
            recipients.append(cc_email)

        # Send the email
        try:
            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                recipients,
                fail_silently=False
            )
        except Exception as e:
            messages.error(self.request, f"Failed to send email: {str(e)}")
            return self.form_invalid(form)

        # Save message record
        Message.objects.create(
            sender=student_user,
            receiver=teacher.user,
            message=email_message
        )

        messages.success(self.request, "Email sent successfully.")
        return super().form_valid(form)

    
