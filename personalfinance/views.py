from django.shortcuts import render
from django.http import HttpResponse
from personalfinance.models import Tags, RelationshipTag, AssociatedPerson, Budget, Expense
# Create your views here.

def index(request):
	expenses_list = Expense.objects.order_by('Date')
	expenses_dict = {'expenses':expenses_list}
	return render(request, 'personalfinance/index.html', context =expenses_dict)