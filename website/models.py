from django.db import models
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.conf import settings


class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{0} -- {1}".format(self.name, self.subject)

    class Meta:
        verbose_name_plural = 'Enquiries'


def mail_sending(instance, created, sender, *args, **kwargs):
    if created:
        from_email = settings.EMAIL_HOST_USER
        message_text = "This is an enquiry mail from website \"fineleap.co.in\" \n" \
                       "Name : {0}\n Subject: {1}\n Email: {2}\n Message: {3}\n, On: {4}".format(
            instance.name, instance.subject, instance.email, instance.message, str(instance.on)
        )
        send_mail(from_email=from_email, recipient_list=['info@fineleap.co.in'], subject='website query from {0}'.format(instance.name),
                  message=message_text)


post_save.connect(mail_sending, sender=Enquiry)
