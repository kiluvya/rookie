from django.confs.urls  import url
from personalfinance import views

urlpatterns = [
	url(r'^$', views.index, name='index'),	
]