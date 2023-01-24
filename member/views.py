from rest_framework import viewsets

from .models import Member ,ProjectRecord
from .serializers import MemberSerializer,ProjectRecordSerializer


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class ProjectRecordViewSet(viewsets.ModelViewSet):
    queryset = ProjectRecord.objects.all()
    serializer_class = ProjectRecordSerializer
