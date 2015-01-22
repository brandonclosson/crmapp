from django.contrib import admin
from .models import Account

def make_clone(modeladmin, request, queryset):
	for obj in queryset:
		account = Account(name=obj.name, phone=obj.phone, address_one=obj.address_one,
						  city=obj.city, state=obj.state, owner=obj.owner)
		account.save()

class AccountAdmin(admin.ModelAdmin):
	actions = [make_clone]


admin.site.register(Account, AccountAdmin)
