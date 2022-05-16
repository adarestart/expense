from rest_framework import serializers
from .models import UserInfo, ExpenseCategory, ExpenseInfo, IncomeCategory, IncomeInfo, Query

class UserSerializer(serializers.ModelSerializer):
    #middleName = serializers.CharField(required = False)   
    
    class Meta:
        model = UserInfo
        fields = '__all__'
        #fields = ('id','firstName','middleName','lastName','email','phone','balance')

class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = '__all__'


class IncomeCategorySerializer(serializers.ModelSerializer): 

    class Meta:
        model = IncomeCategory
        fields = '__all__'

class ExpenseSerializer(serializers.ModelSerializer):   
    class Meta:
        model = ExpenseInfo
        fields = '__all__'

class IncomeSerializer(serializers.ModelSerializer):   
    class Meta:
        model = IncomeInfo
        fields = '__all__'

class QuerySerializer(serializers.ModelSerializer):   
    class Meta:
        model = Query
        fields = ('id','date','amount')

class QueryCatSerializer(serializers.ModelSerializer):   
    class Meta:
        model = Query
        fields = ('id','category','amount')