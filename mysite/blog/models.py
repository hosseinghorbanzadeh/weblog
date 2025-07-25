from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True, null=True)
    message = models.TextField()  
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-created_date']
    def __str__(self):
        return self.subject if self.subject else "No subject"
    


class Newsletter(models.Model):
    email = models.EmailField()
    def __str__(self):
        return self.email

    
