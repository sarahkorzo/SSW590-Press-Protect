from django.db import models
from auditlog.models import AuditlogHistoryField
from auditlog.registry import auditlog

class NewsItem(models.Model):
  title = models.CharField(max_length=255)
  content = models.TextField()
  embargo_date = models.DateTimeField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  history = AuditlogHistoryField()

auditlog.register(NewsItem)

