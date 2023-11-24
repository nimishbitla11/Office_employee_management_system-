from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=100)

    # This is added to display values and make them visible in django administration site
    def __str__(self):
        return self.name 

class Role(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dept = models.ForeignKey(Department, on_delete=models.CASCADE)
    salary = models.IntegerField(default=0)
    bonus = models.IntegerField(default=0)
    role  = models.ForeignKey(Role, on_delete=models.CASCADE)
    phone = models.IntegerField(default=0)
    hire_date = models.DateField()

    def __str__(self):
        return "%s %s %s" %(self.first_name, self.last_name, self.role)

    # def __str__(self):
    #     return self.first_name 
    
    # def __str__(self):
    #     return self.last_name
    
    # def __str__(self):
    #     return self.role


    