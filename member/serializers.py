from rest_framework import serializers

from member.models import Member,ProjectRecord


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ["id", "name",]

class ProjectRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectRecord
        fields = ["id", "project_abstract",]
