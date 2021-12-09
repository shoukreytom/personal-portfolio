from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from portfolio.models import Portfolio, Screenshot


class PortfolioSerializer(ModelSerializer):
    tools = serializers.StringRelatedField(many=True)
    class Meta:
        model = Portfolio
        fields = '__all__'


class ScreenshotSerializer(ModelSerializer):
    class Meta:
        model = Screenshot
        fields = '__all__'
