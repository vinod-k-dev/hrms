from common.common_view_imports import *
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from employees.serializers import *
from employees.models import KycDetail


class KycDetailViewSet(viewsets.ModelViewSet):

    """
    KycDetail Operation View

    KycDetail can perform CRUD operation to the system.
    The data required are "employee", "document_type".
    """

    queryset = KycDetail.objects.all()
    serializer_class = KycDetailSerializer
    permission_classes = [
        IsAuthenticated,
    ]
    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
        DjangoFilterBackend,
    ]
    search_fields = ["employee", "document_type"]
    ordering_fields = "__all__"
    swagger_tag = ["KycDetails"]

    """Modelviewset by default provide CRUD If we need some extra custom functionality then we can override below methods"""
    # def create(self, request):
    #     serializer = self.serializer_class(data=request.data)
    #     if serializer.is_valid():
    #         self.perform_create(serializer)
    #         return return_response(
    #             serializer.data,
    #             True,
    #             "KycDetail Successfully Created!",
    #             status.HTTP_200_OK,
    #         )

    #     return return_response(
    #         serializer.errors, False, "Bad request!", status.HTTP_400_BAD_REQUEST
    #     )

    # def list(self, request, *args, **kwargs):
    #     queryset = self.filter_queryset(self.get_queryset())

    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)

    #     serializer = self.get_serializer(queryset, many=True)
    #     return return_response(
    #         serializer.data,
    #         True,
    #         "KycDetail List Successfully Retrieved!",
    #         status.HTTP_200_OK,
    #     )

    # def retrieve(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)

    #     return return_response(
    #         serializer.data,
    #         True,
    #         "KycDetail Successfully Retrieved!",
    #         status.HTTP_200_OK,
    #     )

    # def update(self, request, *args, **kwargs):
    #     partial = kwargs.pop("partial", False)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     if serializer.is_valid():
    #         self.perform_update(serializer)
    #         return return_response(
    #             serializer.data,
    #             True,
    #             "KycDetail Successfully Updated!",
    #             status.HTTP_200_OK,
    #         )

    #     return return_response(
    #         serializer.errors, False, "Bad request!", status.HTTP_400_BAD_REQUEST
    #     )

    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.is_deleted = True
    #     instance.save()
    #     # self.perform_destroy(instance)
    #     return return_response(
    #         {"detail": "object deleted"},
    #         True,
    #         "KycDetail Successfully Deleted!",
    #         status.HTTP_200_OK,
    #     )
