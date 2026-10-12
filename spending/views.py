from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication,permissions

from spending.permission import IsOwner


from spending.models import Expense
from spending.serailizer import UserSerializer,ExpenseSerializer


class SignUpView(APIView):

    def post(self,request):

        from_data = request.data

        serializer_instants = UserSerializer(data=from_data)

        if serializer_instants.is_valid():

            cleaned_data = serializer_instants.validated_data

            user_object = User.objects.create_user(**cleaned_data)

            serializer_instants = UserSerializer(user_object)

            return Response(data=serializer_instants.data)

        else:
            return Response(data=serializer_instants.errors)

class GetMeView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]


    def get(self,request):
 
        auth_user = request.user

        instance = User.objects.get(username=auth_user)

        serializer_instants = UserSerializer(instance)

        return Response(data=serializer_instants.data)

class ExpenselistCreatView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [permissions.IsAuthenticated]

    def get(self,request):

        request.user

        instants = Expense.objects.filter(owner=request.user)

        serializer_instants =ExpenseSerializer(instants,many = True)

        return Response(data=serializer_instants.data)

    def post(self,requset):

        form_data = requset.data

        serializer_instant = ExpenseSerializer(data=form_data)

        if serializer_instant.is_valid():

            serializer_instant.save(owner=requset.user)

            return Response(data=serializer_instant.data)

        return Response(data=serializer_instant.errors)    


class ExpenseRetrieveUpdateDeleteView(APIView):

    authentication_classes = [authentication.TokenAuthentication]

    permission_classes = [IsOwner]

    def get(self,request,pk=None):

        instance = get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,instance)

        serializer_instants = ExpenseSerializer(instance)

        return Response(data=serializer_instants.data)

    def put(self,request,pk=None):

        instance = get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,instance)

        form_data = request.data

        serilaizer_instants = ExpenseSerializer(data=form_data,instance=instance)

        if serilaizer_instants.is_valid():

            serilaizer_instants.save()

            return Response(data=serilaizer_instants.data)

        else:

            return Response(data=serilaizer_instants.errors)

    def delete(self,request,pk=None):

        instance = get_object_or_404(Expense,id=pk)

        self.check_object_permissions(request,instance)

        instance.delete()

        return Response(data="message:deleted")


            