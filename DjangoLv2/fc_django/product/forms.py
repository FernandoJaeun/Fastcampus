from django import forms

from django.db.utils import IntegrityError

from .models import Product

# Class-based-Views

class RegistrationForm(forms.Form):
    name = forms.CharField(
        error_messages = {
            'required' : '상품명을 입력해주세요.'
        },
        max_length = 32,
        label = '상품명'
    )

    price = forms.IntegerField(
        error_messages = {
            'required' : '가격을 입력해주세요.'
        },
        label = '가격'
    )

    description = forms.CharField(
        error_messages = {
            'required' : '상품 설명을 입력해주세요.'
        },
        label = '상품 설명'
    )
    
    stock = forms.IntegerField(
        error_messages = {
            'required' : '재고를 입력해주세요.'
        },
        label = '재고'
    )

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')
        price = cleaned_data.get('price')
        description = cleaned_data.get('description')
        stock = cleaned_data.get('stock')

        try:
            Product.objects.get(name = name)
            self.add_error('name', '이미 존재하는 상품입니다.')
        except :
            if name and price and description and stock:
                product = Product(
                    name = name,
                    price = price,
                    description = description,
                    stock = stock
                )
                product.save()
            else:
                self.add_error('name', '모두 입력 해주세요.')