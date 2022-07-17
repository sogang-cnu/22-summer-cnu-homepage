from django.db import models
from .undergraduate import *

class Member(models.Model):
    """학회원 클래스 :: cnu 학회원은 학부생에 한정"""

    # Fields
    undergraduate = models.OneToOneField(Undergraduate, on_delete=models.CASCADE)
    joined_at = models.DateTimeField()

    # Methods
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f"{self.undergraduate.student_code}{self.undergraduate.name}"