# -*- coding: utf-8 -*-
#Copyright (C) 2011 Seán Hayes

#SEE LICENSE file

#Python imports
from datetime import datetime

#Django imports
from django.conf import settings
from django.core.mail import EmailMessage
from django.db import models
from django.db.models.signals import post_save

# Create your models here.

class TestEmail(models.Model):
	added = models.DateTimeField(auto_now_add=True)
	
	#email fields
	date = models.DateTimeField(
		default=lambda: datetime.now(),
		help_text="The date you want to set as the date header."
	)
	from_email = models.EmailField(
		'from',
		default=lambda: settings.DEFAULT_FROM_EMAIL
	)
	to = models.TextField()
	bcc = models.TextField()
	subject = models.CharField(
		max_length=150,
		default="This is a test email."
	)
	body = models.TextField(default="Here's some default text.")
	
	def send(self):
		to = self.to.split(',')
		bcc = self.bcc.split(',')
		
		email = EmailMessage(self.subject, self.body, self.from_email, to, bcc)
		email.send()
	
	def __unicode__(self):
		return self.subject
	
	class Meta:
		ordering = ['added']

def test_email_save_handler(sender, instance, created, **kwargs):
	if created:
		instance.send()
post_save.connect(test_email_save_handler, sender=TestEmail)

