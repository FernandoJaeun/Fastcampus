from django.shortcuts import render
from django.views.generic import ListView, FormView, DetailView
from django.utils.decorators import method_decorator

from fcuser.decorators import login_required, admin_required

from .models import Product
from .forms import RegistrationForm
from order.forms import OrderForm

# Create your views here.
def product_main(request):
    return render(request, 'product_main.htm')

# 상품 목록(리스트 형식)
class ProductList(ListView):
    model = Product
    template_name = 'product_list.htm'
    context_object_name = 'product_list'

# 상품 등록
@method_decorator(admin_required, name = 'dispatch')
class ProductRegistration(FormView):
    template_name = 'product_registration.htm'
    form_class = RegistrationForm
    success_url = '/product/'

# 상품 상세
class ProductDetail(DetailView):
    template_name = 'product_detail.htm'
    queryset = Product.objects.all()
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        context =super().get_context_data(**kwargs) # 이 클래스의 context_object_name 이 먼저 데이터를 추가한 뒤 발동됨
        context['form'] = OrderForm(self.request)
        return context
