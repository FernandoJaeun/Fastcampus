from django import forms

from django.db import transaction

from .models import Order
from product.models import Product
from fcuser.models import Fcuser



# Class-based-Views
class OrderForm(forms.Form):
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.request = request  

    quantity = forms.IntegerField(
        error_messages={
            'required': '수량을 입력해주세요.'
        },
        label="수량"
    )

    product = forms.IntegerField(
        error_messages={
            'required':  '상품설명을 입력해주세요.'
        },
        widget=forms.HiddenInput, label='상품설명'
    )

    def clean(self):
        cleaned_data = super().clean()  # 입력 형식을 충족한 데이터
        quantity = cleaned_data.get('quantity')
        product = cleaned_data.get('product')
        fcuser = self.request.session.get('user')

        if quantity and product and fcuser :
            with transaction.atomic():
                prod = Product.objects.get(pk = product)
                order = Order(
                    quantity = quantity,
                    product = prod,
                    fcuser = Fcuser.objects.get(email = fcuser)
                )

                prod.stock -= quantity # 재고 - 주문수량
                print(prod.stock)
                print(order.quantity)
                prod.save()
                order.save() 
        else:
            self.product = product
            self.add_error('quantity', '값이 없습니다.')
            self.add_error('product', '값이 없습니다.')
