from django.db import models
from django.conf import settings
import companies
# Create your models here.
class Application(models.Model):
    class Status(models.TextChoices):
        APPLIED    = 'APPLIED',    'Applied'
        ASSESSMENT = 'ASSESSMENT', 'Assessment'
        INTERVIEW  = 'INTERVIEW',  'Interview'
        OFFER      = 'OFFER',      'Offer'
        REJECTED   = 'REJECTED',   'Rejected'
        
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='applications')
    company = models.ForeignKey(companies.Company,
                                on_delete=models.CASCADE,
                                related_name='applications')
    job_title    = models.CharField(max_length=200)
    status       = models.CharField(
                       max_length=20,
                       choices=Status.choices,
                       default=Status.APPLIED
                   )
    applied_date = models.DateField()
    job_url      = models.URLField(blank=True)
    salary_min   = models.PositiveIntegerField(null=True, blank=True)
    salary_max   = models.PositiveIntegerField(null=True, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-applied_date']

    def __str__(self):
        return f'{self.job_title} at {self.company.name}'