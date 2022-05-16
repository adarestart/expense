from django.urls import path
from .views import UserView, ExpenseCategoryView, ExpenseView, IncomeCategoryView, IncomeView, SingleUserView,QueryView, QueryCatView

urlpatterns = [
    path('users/', UserView.as_view()),
    path('users/<int:user_id>/', SingleUserView.as_view()),
    path('expense_categories/',ExpenseCategoryView.as_view()),
    path('income_categories/',IncomeCategoryView.as_view()),
    path('expenses/', ExpenseView.as_view()),
    path('incomes/', IncomeView.as_view()),
    # group expense by month
    path('queries/', QueryView.as_view()),
    # group expense by category
    path('cat_queries/', QueryCatView.as_view()),

]
