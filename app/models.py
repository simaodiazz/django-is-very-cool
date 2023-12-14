from django.db.models import Model, CharField, ForeignKey, CASCADE
from django.db.models.signals import pre_save
from django.dispatch import receiver

from bcrypt import gensalt, hashpw

# Create your models here.
class User(Model):
    name = CharField(max_length=32)
    password = CharField(max_length=64)

    def __json__(self):
        return {
            'id': self.pk,
            'name': self.name,
            'password': self.password
        }

@receiver(signal=pre_save, sender=User)
def pre_save_author(sender, instance, **kwargs):
    instance.password = hashpw(instance.password.encode('utf-8'), gensalt()).decode('utf-8')

class Message(Model):
    content = CharField(max_length=1024)
    author = ForeignKey(User, on_delete=CASCADE) # Quando o registro associado for excluído, o registro atual também será excluído

    def __json__(self):
        return {
            'id': self.pk,
            'content': self.content,
            'author': self.author
        }
 