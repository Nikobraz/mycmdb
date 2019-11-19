from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse
from cmdb.models import *
# Create your views here.


class BaseView(ListView):
    model = Asset
    template_name = 'table.html'
    context_object_name = 'data'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self):
        return Asset.objects.all()


class AddAsset(CreateView):
    model = Asset
    template_name = 'add.html'
    fields = ['hostname', 'max_ports', 'ports']

    def get_success_url(self):
        return reverse('baseview')

    def form_valid(self, form):
        #reverseddata = dict(switch_port=form.cleaned_data['server_port'], server_port=form.cleaned_data['switch_port'])
        #Port.objects.create(**reverseddata)
        print('Add: ', str(form.cleaned_data))
        return super(AddAsset, self).form_valid(form)


class UpdateAsset(UpdateView):
    model = Asset
    template_name = 'edit.html'
    fields = ['hostname', 'max_ports', 'ports']
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('baseview')

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs()
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def form_valid(self, form):
        #reverseddata = dict(switch_port=form.cleaned_data['server_port'], server_port=form.cleaned_data['switch_port'])
        linkto = list(form.cleaned_data['ports'].values_list('hostname', flat=True))
        linkfrom = form.cleaned_data['hostname']
        reverseddata = dict()
        for item in linkto:
            reverseddata=
        print('Update: ', str(form.cleaned_data['hostname']))
        return super(UpdateAsset, self).form_valid(form)


class AddPort(CreateView):
    model = Port
    template_name = 'addport.html'
    fields = ['server_port', 'switch_port']

    def get_queryset(self):
        return super(AddPort, self).get_queryset()

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs()
        print(kwargs)
        return kwargs
#{'initial': {}, 'prefix': None, 'data': <QueryDict: {'csrfmiddlewaretoken': ['HVAC0B0MXLSNtA7PqeNOZSbq69XWmf8tKrBWCIvqYEikNQW6fB6ex0D2Ief4ENPi'],
    # 'server_port': ['1'], 'switch_port': ['6']}>, 'files': <MultiValueDict: {}>, 'instance': None}

    def form_valid(self, form):
        reverseddata = dict(switch_port=form.cleaned_data['server_port'], server_port=form.cleaned_data['switch_port'])
        Port.objects.create(**reverseddata)
        return super(AddPort, self).form_valid(form)

    def get_success_url(self):
        return reverse('baseview')

    def cleaned_data(self):
        pass

