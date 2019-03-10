from django import forms
from product.models import Product

from django.core import serializers
from product.models import Payment

class ProductForm(forms.ModelForm):
	class Meta:
		model = Product
		fields = "__all__"

class PaymentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Payment
		fields = "__all__"
