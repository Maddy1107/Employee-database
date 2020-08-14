from django.contrib import admin
from .models import Employee,family,med,emergency,education,employment,references


admin.site.register(Employee)
admin.site.register(family)
admin.site.register(med)
admin.site.register(emergency)
admin.site.register(education)
admin.site.register(employment)
admin.site.register(references)
