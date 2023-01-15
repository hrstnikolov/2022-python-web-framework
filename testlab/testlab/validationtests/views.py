from django.urls import reverse_lazy
from django.views import generic as views

from testlab.validationtests.models import ValidationTest


class ValidationTestCreateView(views.CreateView):
    model = ValidationTest
    template_name = 'validationtests/validationtest-add-template.html'
    fields = '__all__'
    success_url = reverse_lazy('list validation tests')


class ValidationTestListView(views.ListView):
    model = ValidationTest
    template_name = 'validationtests/validationtest-list-template.html'
    fields = '__all__'
