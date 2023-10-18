from rest_framework import serializers
from .models import Client, Scope, Grant_types, Response_types

class ClientSerializer(serializers.Serializer):
  id = serializers.IntegerField(read_only=True)
  client_secret = serializers.CharField(required=True, allow_blank=False, max_length=64)
  browser_redirect = serializers.BooleanField(default=True)
  provider_name = serializers.CharField(required=True, allow_blank=False, max_length=255)
  client_id = serializers.CharField(required=True, allow_blank=False, max_length=64)
  redirect_uri = serializers.CharField(required=True, allow_blank=False, max_length=255)
  implicit_consent = serializers.BooleanField(default=False)
  response_types = serializers.PrimaryKeyRelatedField(many=True, queryset=Response_types.objects.all())
  grant_types = serializers.PrimaryKeyRelatedField(many=True, queryset=Grant_types.objects.all())
  scope = serializers.PrimaryKeyRelatedField(many=True, queryset=Scope.objects.all())
  
  def create(self, validated_data):
    """
    Create and return a new `Client` instance, given the validated data.
    """
    return Client.objects.create(**validated_data)
  
  def update(self, instance, validated_data):
    """
    Update and return an existing `Client` instance, given the validated data.
    """
    instance.client_secret = validated_data.get('client_secret', instance.client_secret)
    instance.browser_redirect = validated_data.get('browser_redirect', instance.browser_redirect)
    instance.provider_name = validated_data.get('provider_name', instance.provider_name)
    instance.client_id = validated_data.get('client_id', instance.client_id)
    instance.redirect_uri = validated_data.get('redirect_uri', instance.redirect_uri)
    instance.implicit_consent = validated_data.get('implicit_consent', instance.implicit_consent)
    instance.response_types = validated_data.get('response_types', instance.response_types)
    instance.grant_types = validated_data.get('grant_types', instance.grant_types)
    instance.scope = validated_data.get('scope', instance.scope)
    instance.save()
    return instance