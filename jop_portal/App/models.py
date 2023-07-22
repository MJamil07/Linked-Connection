from django.db import models

# Create your models here.
# 'http://127.0.0.1:8000/home/'
class SignUpUser(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    email = models.EmailField()
    password = models.TextField()
    college_name = models.TextField()
    qualification = models.TextField()
    phone = models.BigIntegerField()
    
    def __str__(self) -> str:
        return self.first_name + self.last_name
    



class Jops(models.Model):
    company_name = models.TextField()
    position = models.TextField()
    skills = models.TextField()
    describtion = models.TextField()
    qualification = models.TextField()

    def __str__(self) -> str:
        return self.company_name
    
class AppCompanies(models.Model):
    name =  models.TextField()
    size =  models.IntegerField()
    head =  models.TextField()
    about =  models.TextField()
    based =  models.TextField()
    products =  models.TextField()
    website =  models.TextField()
    gmail =  models.CharField(max_length = 30 , unique = True)
    password =  models.TextField()
    phone =  models.TextField()
    type =  models.TextField()
    logo =  models.ImageField(upload_to = 'media/logo')
    
    def __str__(self) -> str:
        return self.name
    
class Job_Posts(models.Model):
    position = models.TextField()
    type = models.TextField()
    description = models.TextField()
    location = models.TextField()
    post_date = models.DateField(auto_now = True)
    responsibility = models.TextField()
    basic_qualification = models.TextField()
    preffered_qualification = models.TextField()
    companie = models.ForeignKey(AppCompanies , on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.position
    
class Apply_jop(models.Model):

    name = models.TextField()
    skills = models.TextField()
    user = models.ForeignKey(SignUpUser , on_delete = models.CASCADE)
    jop_post = models.ForeignKey(Job_Posts , on_delete = models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
class UserFollow(models.Model):

    froms = models.EmailField()
    to = models.EmailField()
    
    def __str__(self) -> str:
        return f' from {self.froms} , to {self.to}';

class Post(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to='posts/')
    user = models.ForeignKey(SignUpUser , on_delete = models.CASCADE , null = True)
    companie = models.ForeignKey(AppCompanies , on_delete = models.CASCADE , null = True)

    def __str__(self):

        return f' {self.description} '