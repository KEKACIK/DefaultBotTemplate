from django.contrib import admin

from admin_web.admin import admin_site
from admin_web.models import Users


@admin.register(Users, site=admin_site)
class UsersAdmin(admin.ModelAdmin):
    list_display = ("id", "username", "is_admin", "created_at")
    list_filter = ("is_admin",)
    readonly_fields = ("id", "created_at")
    # search_fields = ()
    # list_editable = ()

    def has_add_permission(self, request):
        return False
