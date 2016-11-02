from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Answer


@receiver(post_save, sender=Answer)
@receiver(post_delete, sender=Answer)
def refresh_count(instance, **kwargs):
	question = instance.question
	question.save()
	
    