import csv
from io import StringIO

from django.http import FileResponse
from rest_framework import status, viewsets
from rest_framework.response import Response

import urllib.parse

from .models import Member, ProjectRecord
from .serializers import MemberSerializer, ProjectRecordSerializer


def create_csv(project_Records, limit):
    csv_file = StringIO()
    fieldnames = ["開始", "終了", "案件概要", "案件詳細"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for project_Record in project_Records[:limit]:
        writer.writerow(
            {
                "開始": str(project_Record.start_date),
                "終了": str(project_Record.end_date),
                "案件概要": project_Record.project_abstract,
                "案件詳細": project_Record.project_detail,
            }
        )
    return csv_file


def csv_download_view(request):
    project_Records = ProjectRecord.objects.all().order_by("-start_date")

    filename = "レポート.csv"
    quoted_filename = urllib.parse.quote(filename)

    csv_file = create_csv(project_Records, 10)
    response = FileResponse(csv_file.getvalue(), content_type='text/csv; charset=Shift-JIS')
    response['Content-Disposition'] = f'attachment; filename={quoted_filename}'

    return response


class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer


class ProjectRecordViewSet(viewsets.ModelViewSet):
    queryset = ProjectRecord.objects.all().order_by("-start_date")
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
