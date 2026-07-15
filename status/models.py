from django.db import models

# Create your models here.
class userDetails(models.Model):
    name=models.CharField(max_length=200)
    age=models.IntegerField()
    address=models.CharField(max_length=200)
    phone=models.IntegerField()
    email=models.EmailField()

    def __str__(self):
        return self.name
    

class Status(models.Model):
    title=models.CharField(max_length=200)
    subtitle=models.CharField(max_length=200)
    description= models.TextField(blank=True, null=True)
    upload_time=models.DateTimeField(auto_now_add=True)
    image=models.ImageField(upload_to='',null=True,blank=True)
    users=models.ForeignKey(userDetails,related_name='status',on_delete=models.CASCADE)