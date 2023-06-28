from .models  import Vino
from rest_framework.serializers import ModelSerializer


class  VinoSerializer(ModelSerializer):
    class Meta:
        model = Vino
        fields = "__all__"