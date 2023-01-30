from rest_framework import status, viewsets
from rest_framework.response import Response

from .models import Member, ProjectRecord
from .serializers import MemberSerializer, ProjectRecordSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class ProjectRecordViewSet(viewsets.ModelViewSet):
    queryset = ProjectRecord.objects.all()
    serializer_class = ProjectRecordSerializer

    # POST
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid():
            print(serializer.errors)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )
