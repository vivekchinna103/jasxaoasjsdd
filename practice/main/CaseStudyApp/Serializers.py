from rest_framework import serializers
from CaseStudyApp.models import CaseStudies

class CaseStudySerializers(serializers.ModelSerializer):
    class Meta:
        model= CaseStudies
        fields="__all__"