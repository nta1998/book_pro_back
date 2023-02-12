from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import BooksSerializer, CustomersSerializer, LoansSerializer
from .models import Books, Customers, Loans
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status
from rest_framework.views import APIView

@api_view(['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
def books_crud(req, id=-1):
    if req.method == 'GET':
        if int(id) > -1:
            try:
                temp_task = Books.objects.get(id=int(id))
                return Response(BooksSerializer(temp_task, many=False).data)
            except Books.DoesNotExist:
                return Response("not found")
        all_tasks = BooksSerializer(Books.objects.all(), many=True).data
        return Response(all_tasks)
    if req.method == 'POST':
        print(req.data)
        tsk_serializer = BooksSerializer(data=req.data)
        if tsk_serializer.is_valid():
            tsk = tsk_serializer.save()
            if req.FILES.get('image'):
                tsk.image = req.FILES['image']
                tsk.save()
            return Response("post...")
        else:
            return Response(tsk_serializer.error_messages)
    # if req.method == 'POST':
    #     tsk_serializer = BooksSerializer(data=req.data)
    #     if tsk_serializer.is_valid():
    #         tsk_serializer.save()
    #         return Response("post...")
    #     else:
    #         return Response(tsk_serializer.error_messages)
    if req.method == 'DELETE':
        try:
            temp_task = Books.objects.get(id=int(id))
        except Books.DoesNotExist:
            return Response("not found")

        temp_task.delete()
        return Response("del...")
    if req.method == 'PUT':
        try:
            temp_task = Books.objects.get(id=int(id))
        except Books.DoesNotExist:
            return Response("not found")

        ser = BooksSerializer(data=req.data)
        old_task = Books.objects.get(id=int(id))
        res = ser.update(old_task, req.data)
        return Response("Put...")


@api_view(['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
def customer_crud(req, id=-1):
    if req.method == 'GET':
        if int(id) > -1:
            try:
                temp_task = Customers.objects.get(id=int(id))
                return Response(CustomersSerializer(temp_task, many=False).data)
            except Customers.DoesNotExist:
                return Response("not found")
        all_tasks = CustomersSerializer(
            Customers.objects.all(), many=True).data
        return Response(all_tasks)
    if req.method == 'POST':
        tsk_serializer = CustomersSerializer(data=req.data)
        if tsk_serializer.is_valid():
            tsk_serializer.save()
            return Response("post...")
        else:
            return Response(tsk_serializer.error_messages)
    if req.method == 'DELETE':
        try:
            temp_task = Customers.objects.get(id=int(id))
        except Customers.DoesNotExist:
            return Response("not found")

        temp_task.delete()
        return Response("del...")
    if req.method == 'PUT':
        try:
            temp_task = Customers.objects.get(id=int(id))
        except Customers.DoesNotExist:
            return Response("not found")

        ser = CustomersSerializer(data=req.data)
        old_task = Customers.objects.get(id=int(id))
        res = ser.update(old_task, req.data)
        return Response("Put...")


@api_view(['GET', 'POST', 'DELETE', 'PUT', 'PATCH'])
def Loans_crud(req, id=-1):
    if req.method == 'GET':
        if int(id) > -1:
            try:
                temp_task = Loans.objects.get(id=id)
                data = LoansSerializer(temp_task, many=False).data
                data['customers_id'] = temp_task.customers_id.Name
                data['BookID'] = temp_task.BookID.Name
                return Response(data)
            except Loans.DoesNotExist:
                return Response("not found")
        all_tasks = LoansSerializer(Loans.objects.all(), many=True).data
        for task in all_tasks:
            task['customers_id'] = Loans.objects.get(
                id=task['id']).customers_id.Name
            task['BookID'] = Loans.objects.get(id=task['id']).BookID.Name
        return Response(all_tasks)
    if req.method == 'POST':
        tsk_serializer = LoansSerializer(data=req.data)
        print(req.data)
        if tsk_serializer.is_valid():
            tsk_serializer.save()
            return Response("post...")
        else:
            return Response(tsk_serializer.error_messages)
    if req.method == 'DELETE':
        try:
            temp_task = Loans.objects.get(id=int(id))
        except Loans.DoesNotExist:
            return Response("not found")

        temp_task.delete()
        return Response("del...")
    if req.method == 'PUT':
        print(req.data)
        try:
            temp_task = Loans.objects.get(id=int(id))
        except Loans.DoesNotExist:
            return Response("not found")

        ser = LoansSerializer(data=req.data)
        old_task = Loans.objects.get(id=int(id))
        res = ser.update(old_task, req.data)
        return Response("Put...")

class APIViews(APIView):
    parser_class=(MultiPartParser,FormParser)
    def post(self,request,*args,**kwargs):
        api_serializer=BooksSerializer(data=request.data)
       
        if api_serializer.is_valid():
            api_serializer.save()
            return Response(api_serializer.data,status=status.HTTP_201_CREATED)
        else:
            print('error',api_serializer.errors)
            return Response(api_serializer.errors,status=status.HTTP_400_BAD_REQUEST)