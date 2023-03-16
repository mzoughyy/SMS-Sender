from django.db import models
import os
from twilio.rest import Client

class Score(models.Model):
    result = models.PositiveIntegerField()

    def __str__(self):
        return str(self.result)
    def save(self,*args,**kwargs):
        if self.result <70:
            account_sid = 'XXXXXXXXXXXXXXXXXXXXXX'
            auth_token = 'XXXXXXXXXXXXXXXXXXXXXXX'
            client = Client(account_sid, auth_token)

            message = client.messages.create(
                              body=f'Your score is: {self.score} ',
                              from_='+xxxxxxx',
                              to='+xxxxxx'
                          )

            print(message.sid)
        return super().save(*args,**kwargs)
    
        