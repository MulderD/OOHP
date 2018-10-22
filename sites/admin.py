from django.contrib import admin

from .models import SiteDetail, WMO, Aviation, Comms, Radar, AWS, NetworkDevice

admin.site.register(SiteDetail)
admin.site.register(WMO)
admin.site.register(Aviation)
admin.site.register(Comms)
admin.site.register(Radar)
admin.site.register(AWS)
admin.site.register(NetworkDevice)

