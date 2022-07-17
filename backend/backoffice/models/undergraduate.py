from django.db import models
from django.core.validators import RegexValidator

class Undergraduate(models.Model):
    """학부생 클래스 :: cnu 지원자 및 회원은 학부생에 한정"""

    phone_number_regex = RegexValidator(regex=r'^[0-9]{3}[0-9]{4}[0-9]{4}$')

    # Fields
    student_code = models.IntegerField(help_text="학번", unique=True)
    name = models.CharField(max_length=16, help_text="이름")
    phone_number = models.CharField(max_length=11, validators=[phone_number_regex], help_text="휴대전화번호")

    # Metadata
    class Meta:
        ordering = ['student_code']

    # Methods
    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return f"{self.student_code}{self.name}"