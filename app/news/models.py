from django.db import models
from book.models import Faculty
from django.utils.translation import gettext_lazy as _



class News(models.Model):
    title = models.CharField(max_length=200)
    summary = models.TextField()
    details = models.TextField()
    news_reference = models.CharField(max_length=255)
    news_title_persian = models.CharField(max_length=200)
    news_summary_persian = models.TextField()
    news_reference_persian = models.CharField(max_length=255)
    date = models.DateField()
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")