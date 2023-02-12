from django.db import models


# Create your models here.
class Customers(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=35)
    Age = models.IntegerField()
    City = models.CharField(max_length=35)
    active = models.BooleanField()


    def __str__(self):
        return self.sName
class Books(models.Model):
    id = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=35)
    Author = models.CharField(max_length=35)
    Year_Published = models.DateField()
    Type = models.IntegerField()
    image = models.ImageField(null=True,blank=True,default='no_book_img.png')
    active = models.BooleanField()




class Loans(models.Model):
    id = models.AutoField(primary_key=True)
    Loandate = models.DateField()
    Returndate = models.DateField()
    BookID = models.ForeignKey(Books,on_delete=models.CASCADE,null=True)
    customers_id = models.ForeignKey(Customers,on_delete=models.CASCADE,null=True)
    returned = models.BooleanField()


