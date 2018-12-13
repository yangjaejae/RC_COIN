from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Profile


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profiles'
    fk_name = 'user'


class ProfileAdmin(UserAdmin):
    inlines = (ProfileInline, )
    list_display = ('username', 'email', 'gender', 'birth_year', 'birth_month', 'birth_date', 'type', 'status', 'date_joined')
    list_select_related = ('profile',)

    def gender(self, instance):
        return instance.profile.gender

    def birth_year(self, instance):
        return instance.profile.birth_year

    def birth_month(self, instance):
        return instance.profile.birth_month

    def birth_date(self, instance):
        return instance.profile.birth_date

    def type(self, instance):
        return instance.profile.type

    def status(self, instance):
        return instance.profile.status

    def date_joined(self, instance):
        return instance.profile.date_joined

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(ProfileAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, ProfileAdmin)
