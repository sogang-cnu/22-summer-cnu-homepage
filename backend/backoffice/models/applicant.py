from django.db import models
from .undergraduate import *

class Applicant(models.Model):
    """지원자 클래스 :: cnu 지원자는 학부생에 한정"""

    # Fields
    undergraduate = models.OneToOneField(Undergraduate, on_delete=models.CASCADE)
    applied_at = models.DateTimeField()

    # Methods
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f"{self.undergraduate.student_code}{self.undergraduate.name}"