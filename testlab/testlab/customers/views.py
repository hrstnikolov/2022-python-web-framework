from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views
from django import forms
from testlab.customers.models import Customer


class CustomerCreateForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name',)


class CustomerCreateView(views.CreateView):
    model = Customer
    form_class = CustomerCreateForm
    template_name = 'customers/customer-add-template.html'
    success_url = reverse_lazy('list customers')


class CustomerListView(views.ListView):
    model = Customer
    template_name = 'customers/customer-list-template.html'
    fields = '__all__'
