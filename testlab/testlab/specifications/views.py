from django.urls import reverse_lazy
from django.views import generic as views

from testlab.customers.models import Customer
from testlab.specifications.models import Specification


class SpecificationCreateView(views.CreateView):
    model = Specification
    template_name = 'specifications/specification-add-template.html'
    fields = '__all__'
    success_url = reverse_lazy('list specifications')


class SpecificationListView(views.ListView):
    model = Specification
    template_name = 'specifications/specification-list-template.html'
    fields = '__all__'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        # add pattern to context to be assigned to the <input> `value` attribute
        context['pattern'] = self.__get_search_pattern()

        context['customers'] = Customer.objects.values_list('name', flat=True)

        return context

    def get_queryset(self):
        queryset = super().get_queryset()
        # filtering the query set results
        pattern = self.__get_search_pattern()
        if pattern:
            # combining querysets
            queryset = queryset.filter(customer__name__icontains=pattern) \
                       | queryset.filter(name__icontains=pattern)
        return queryset

    def __get_search_pattern(self):
        search_pattern = self.request.GET.get(key='pattern', default='')
        return search_pattern


class SpecificationListByCustomerView(views.ListView):
    model = Specification
    template_name = 'specifications/specification-list-template.html'
    fields = '__all__'

    def get_queryset(self):
        queryset = super().get_queryset()
        customer = self.request.GET.get('customer', None)
        queryset = queryset.filter(customer__name__iexact=customer)

        return queryset


class SpecificationDetailsView(views.DetailView):
    model = Specification
    template_name = 'specifications/specification-details-template.html'
