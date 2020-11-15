from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator


from fcuser.decorators import login_required

from .forms import OrderForm
from .models import Order
@method_decorator(login_required, name = 'dispatch')
class OrderCreate(FormView):
    form_class = OrderForm
    success_url = '/product/list'

    def form_invalid(self, form):
        return redirect('/product/list/' + str(form.product))

    def get_form_kwargs(self, **kwargs):
        kwargs = super().get_form_kwargs(**kwargs)
        kwargs.update({
            'request' : self.request
        })
        return kwargs

@method_decorator(login_required, name = 'dispatch')
class OrderList(ListView):  
    template_name = 'order_list.htm'
    context_object_name = 'order_list'

    def get_queryset(self, **kwargs):
        queryset = Order.objects.filter(fcuser__email = self.request.session.get('user'))
        return queryset