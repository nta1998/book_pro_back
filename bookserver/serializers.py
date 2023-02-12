from rest_framework import serializers
from .models import Books, Customers, Loans


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'

    def create(self, validated_data):
        return Books.objects.create(**validated_data)


class CustomersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'

    def create(self, validated_data):
        return Customers.objects.create(**validated_data)
# class LoansSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Loans
#         fields = '__all__'
#     def create(self, validated_data):
#         return Loans.objects.create(**validated_data)
class LoansSerializer(serializers.ModelSerializer):

    class Meta:
        model = Loans
        fields = ['id', 'customers_id', 'BookID', 'Loandate', 'Returndate', 'returned']
    def create(self, validated_data):
        return Loans.objects.create(**validated_data)