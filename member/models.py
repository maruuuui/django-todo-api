from django.db import models


class Member(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField("氏名", max_length=20)

    def __str__(self) -> str:
        return self.name


class ProjectRecord(models.Model):
    id = models.BigAutoField(primary_key=True)
    member = models.ForeignKey(Member, verbose_name="社員", on_delete=models.CASCADE)
    start_date = models.DateField("開始日", null=True)
    end_date = models.DateField("終了日", null=True)
    project_abstract = models.CharField("案件概要", max_length=50)
    project_detail = models.CharField("案件詳細", max_length=1000, blank=True)

    def __str__(self) -> str:
        return self.project_abstract
