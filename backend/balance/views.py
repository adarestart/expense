from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models.functions import TruncMonth
from .serializers import UserSerializer, ExpenseCategorySerializer, ExpenseSerializer, IncomeCategorySerializer, IncomeSerializer, QuerySerializer, QueryCatSerializer
from .models import UserInfo, ExpenseCategory, ExpenseInfo, IncomeCategory, IncomeInfo, Query

# Create your views here.

class UserView(APIView):
    def get(self, request):
        users = UserInfo.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SingleUserView(APIView):
    def get(self, request,user_id):
        users = UserInfo.objects.get(id=user_id)
        serializer = UserSerializer(users)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    
class ExpenseCategoryView(APIView):
    def get(self, request):
        users = ExpenseCategory.objects.all()
        serializer = ExpenseCategorySerializer(users, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = ExpenseCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncomeCategoryView(APIView):
    def get(self, request):
        users = IncomeCategory.objects.all()
        serializer = IncomeCategorySerializer(users, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = IncomeCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ExpenseView(APIView):
    def get(self, request):
        expense = ExpenseInfo.objects.all()
        serializer = ExpenseSerializer(expense, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = ExpenseSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # also update user balance
            users = UserInfo.objects.get(id=serializer.data['user_id'])
            expense = ExpenseInfo.objects.get(id = serializer.data['id'])
            balance = users.balance
            users.balance=balance-expense.amount
            users.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IncomeView(APIView):
    def get(self, request):
        income = IncomeInfo.objects.all()
        serializer = IncomeSerializer(income, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def post(self, request):  
        print(request.data)
        serializer = IncomeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # also update user balance
            users = UserInfo.objects.get(id=serializer.data['user_id'])
            income = IncomeInfo.objects.get(id = serializer.data['id'])
            balance = users.balance
            users.balance=balance+income.amount
            users.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QueryView(APIView):
    def get(self, request):
        result = ExpenseInfo.objects.raw("select date_format(date,'%%M')as date, sum(amount)as amount,count(id)as id from balance_expenseinfo group by date_format(date,'%%M');");
        serializer = QuerySerializer(result, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

class QueryCatView(APIView):
    def get(self, request):
        result = ExpenseInfo.objects.raw("SELECT count(balance_expenseinfo.id)as id, sum(amount) as amount, name as category FROM balance_expenseinfo JOIN balance_expensecategory WHERE balance_expenseinfo.category_id_id=balance_expensecategory.id GROUP BY category;");
        serializer = QueryCatSerializer(result, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
