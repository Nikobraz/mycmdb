from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse
from .models import Asset, Port
from .serializers import AssetSerializer, PortSerializer
from django.db import IntegrityError
from rest_framework import viewsets
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
    fields = ['hostname', 'max_ports']

    def get_success_url(self):
        return reverse('baseview')

    def form_valid(self, form):
        return super(AddAsset, self).form_valid(form)


class RemoveAsset(DeleteView):
    model = Asset

    def get_success_url(self):
        return reverse('baseview')


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
        linkto = list(form.cleaned_data['ports'].values_list('hostname', flat=True))
        linkfrom = form.cleaned_data['hostname']
        for item in linkto:
            try:
                Port.objects.create(server_port=Asset.objects.get(hostname=linkfrom), switch_port=Asset.objects.get(hostname=item))
                Port.objects.create(server_port=Asset.objects.get(hostname=item), switch_port=Asset.objects.get(hostname=linkfrom))
            except IntegrityError:
                pass
        return super(UpdateAsset, self).form_valid(form)


class AddPort(CreateView):
    model = Port
    template_name = 'addport.html'
    fields = ['server_port', 'switch_port']

    def get_queryset(self):
        return super(AddPort, self).get_queryset()

    def get_form_kwargs(self, *args, **kwargs):
        kwargs = super().get_form_kwargs()
        return kwargs

    def form_valid(self, form):
        """Create reverse relation"""
        reverseddata = dict(switch_port=form.cleaned_data['server_port'], server_port=form.cleaned_data['switch_port'])
        print(reverseddata)
        Port.objects.create(**reverseddata)
        return super(AddPort, self).form_valid(form)

    def get_success_url(self):
        return reverse('baseview')

    def cleaned_data(self):
        pass


class AssetViewSet(viewsets.ModelViewSet):
    queryset = Asset.objects.all().order_by('hostname')
    serializer_class = AssetSerializer


class PortViewSet(viewsets.ModelViewSet):
    queryset = Port.objects.all().order_by('server_port')
    serializer_class = PortSerializer
