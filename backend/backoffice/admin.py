from django.contrib import admin
from .models.undergraduate import Undergraduate
from .models.applicant import Applicant

# Register your models here.
admin.site.register(Undergraduate)
admin.site.register(Applicant)