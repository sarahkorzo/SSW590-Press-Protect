from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from auditlog.models import LogEntry
from .models import CustomUser

#username is admin, pass is test123
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username', 'email', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'role')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2', 'role', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email', 'username', 'role')
    ordering = ('email',)
    
    # Admin action to view audit logs for a selected user
    @admin.action(description='View Audit Logs')
    def view_audit_logs(self, request, queryset):
    for user in queryset:
        logs = LogEntry.objects.filter(actor_object_id=user.id).order_by('-timestamp')
        if logs.exists():
            self.message_user(request, f"Audit logs for {user.username}:")
            for log in logs:
                self.message_user(
                    request,
                    f"Action" {log.get_action_display()}, Date: {log.timestamp}, Changes: {log.changes}"
                )
        else:
            self.message_user(request, f"No audit logs found for {user.username}.")

    actions = ['view_audit_logs'] 

admin.site.register(CustomUser, CustomUserAdmin)
