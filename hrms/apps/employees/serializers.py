from django.db.models import Q
from common.common_serializer_imports import *
from django.contrib.auth import get_user_model

from employees.models import KycDetail

User = get_user_model()


class KycDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = KycDetail
        fields = "__all__"
