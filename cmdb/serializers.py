from .models import Asset, Port
from rest_framework import serializers


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = ['hostname', 'max_ports', 'ports']


class PortSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Port
        fields = ['server_port', 'server_number', 'switch_port', 'switch_number']
