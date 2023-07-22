from django.contrib import admin
from .models import SignUpUser , Jops , AppCompanies , Job_Posts
# Register your models here.


admin.site.register(SignUpUser)
admin.site.register(Jops)
admin.site.register(AppCompanies)
admin.site.register(Job_Posts)
