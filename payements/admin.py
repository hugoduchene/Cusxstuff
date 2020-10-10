from django.contrib import admin

from .models import (
    MethodPayement,
    CommandWait,
    CommandDone,
)

# Register your models here.

admin.site.register(MethodPayement)
admin.site.register(CommandWait)
admin.site.register(CommandDone)