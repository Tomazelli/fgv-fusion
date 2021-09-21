from django.contrib import admin

from .models import Role, Service, Member


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('role', 'modified', 'active')


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service', 'icon', 'active', 'modified')


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('name', 'role', 'bio', 'modified', 'active')