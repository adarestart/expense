from django.db import models
from numpy import require

# Create your models here.


class UserInfo(models.Model):
    firstName = models.CharField(verbose_name="first name", max_length=25)
    middleName = models.CharField(verbose_name="middle name", blank=True,max_length=25)
    lastName = models.CharField(verbose_name="last name", max_length=25)
    email = models.CharField(verbose_name="e-mail address", max_length=30)
    phone = models.CharField(verbose_name="phone number", max_length=10)
    balance = models.DecimalField(verbose_name="account balance", max_digits=10, decimal_places=2, default=0)
    
    class Meta:
        verbose_name = 'User'

    def __str__(self):
        return self.firstName+" "+self.lastName

class ExpenseCategory(models.Model):
    name = models.CharField(verbose_name="category name", max_length=30)
    description = models.CharField(verbose_name="category description", blank=True,max_length=200)
     
    class Meta:
        verbose_name = 'Expense Category'

    def __str__(self):
        return self.name

class IncomeCategory(models.Model):
    name = models.CharField(verbose_name="category name", max_length=30)
    description = models.CharField(verbose_name="category description", blank=True,max_length=200)
     
    class Meta:
        verbose_name = 'Income Category'

    def __str__(self):
        return self.name

 
class ExpenseInfo(models.Model):
    amount = models.DecimalField(verbose_name="expense amount", max_digits=10, decimal_places=2)
    date = models.DateField(verbose_name="expense date")
    description = models.CharField(verbose_name="expense description", blank=True,max_length=50)

    category_id = models.ForeignKey('ExpenseCategory',on_delete=models.SET_DEFAULT,default=1)
    user_id = models.ForeignKey('UserInfo',on_delete=models.CASCADE)
     
    class Meta:
        verbose_name = 'Expense Information'

    def __str__(self):
        return self.amount+" "+self.date

class IncomeInfo(models.Model):
    amount = models.DecimalField(verbose_name="income amount", max_digits=10, decimal_places=2)
    date = models.DateField(verbose_name="income date")
    description = models.CharField(verbose_name="income description", blank=True,max_length=50)

    category_id = models.ForeignKey('IncomeCategory',on_delete=models.SET_DEFAULT,default=1)
    user_id = models.ForeignKey('UserInfo',on_delete=models.CASCADE)
     
    class Meta:
        verbose_name = 'Income Information'

    def __str__(self):
        return self.amount+" "+self.date

class Query(models.Model):
    amount = models.DecimalField(verbose_name="income amount", max_digits=10, decimal_places=2)
    date = models.DateField(verbose_name="income date")
    category = models.CharField(verbose_name="category name", max_length=30)

     
    class Meta:
        verbose_name = 'Query Information'

    def __str__(self):
        return self.amount+" "+self.date