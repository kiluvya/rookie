from django.contrib import admin
from personalfinance.models import Tags, RelationshipTag, AssociatedPerson, Expense, Budget

# Register your models here.

admin.site.register(Expense)
admin.site.register(Tags)
admin.site.register(RelationshipTag)
admin.site.register(AssociatedPerson)
admin.site.register(Budget)