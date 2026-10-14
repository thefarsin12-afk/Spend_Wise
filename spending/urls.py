from django.urls import path
from spending.views import SignUpView
from spending.views import GetMeView
from spending.views import ExpenselistCreatView,ExpenseRetrieveUpdateDeleteView
from rest_framework.authtoken.views import ObtainAuthToken
from spending.views import SummaryView
from spending.views import BudgetPlanView

urlpatterns = [

 # ==== admin section ====
 path('signup/',SignUpView.as_view()),
 path('me/',GetMeView.as_view()),

 # ==== list,post section ====
 path('expenses/',ExpenselistCreatView.as_view()),

 # ==== retrieve,update,delete section ====
 path('expenses/<int:pk>/',ExpenseRetrieveUpdateDeleteView.as_view()),

 #==== summary section ====
 path('expenses/summary/',SummaryView.as_view()),

 # ==== token section ====
 path('token/',ObtainAuthToken.as_view()),

 # ==== budget plan ====
 path('expenses/budget/',BudgetPlanView.as_view()),

     
]