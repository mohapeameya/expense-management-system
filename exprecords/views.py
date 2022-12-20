from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Exprecord
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import ExprecordCreateForm, SearchForm
from django.contrib import messages

from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView
)

from .tables import SimpleTable
from django_tables2 import SingleTableView

from django.db.models import Sum
from django.db.models import Q

@login_required
def home(request):
	total_exp = Exprecord.objects.aggregate(Sum('cost'))
	project_exp = Exprecord.objects.values('project__name').order_by('project').annotate(total_price=Sum('cost'))
	labels1 = []
	data1 = []
	for item in project_exp:
		labels1.append(item['project__name'])
		data1.append(item['total_price'])

	contribution = Exprecord.objects.values('contributor').order_by('contributor').annotate(total_price=Sum('cost'))
	labels2 = []
	data2 = []
	for item in contribution:
		labels2.append(item['contributor'])
		data2.append(item['total_price'])

	context = {
		'total_exp': total_exp,
		'labels1': labels1,
		'data1': data1,
		'labels2': labels2,
		'data2': data2
	}
	return render(request, 'exprecords/home.html', context)

class ExprecordListView(LoginRequiredMixin, SingleTableView):
	model = Exprecord

	table_class = SimpleTable

	# <app>/<model>_list.html --> template naming convention
	template_name = 'exprecords/exprecords.html'

	# if list variable used in list template is not named 'object'(here its 'exprecord'),
	# reset it using context_object_name
	# context_object_name = 'exprecords'
	
	# order list using the object attribute
	# ordering = ['-date']
	
	# records per page
	paginate_by = 7

	# form_class = SearchForm

	 # def post(self, request, *args, **kwargs):
  #       form = self.form_class(request.POST)
  #       if form.is_valid():
  #           # <process form cleaned data>
  #           return form.cleaned


	def get_queryset(self):
		self.query = self.request.GET.get('query','')
		self.sort = self.request.GET.get('sort','')
		exprecords = self.model.objects.all().order_by('-date')
		if self.query:
			exprecords = exprecords.filter(
				Q(project__name__icontains=self.query) |
				Q(item__icontains=self.query) |
				Q(contributor__username__icontains=self.query) |
				Q(cost__icontains=self.query)
			).order_by('-date')
		# cost needs to be compared as a value
		return exprecords

	def get_context_data(self,*args, **kwargs):
		context = super().get_context_data(*args,**kwargs)
		context['query'] = self.query
		context['sort'] = self.sort
		return context



class UserExprecordListView(LoginRequiredMixin, SingleTableView):
	model = Exprecord

	table_class = SimpleTable

	# <app>/<model>_list.html --> template naming convention
	template_name = 'exprecords/exprecords.html'
	
	# if list variable used in list template is not named 'object'(here its 'exprecord'),
	# reset it using context_object_name
	# context_object_name = 'exprecords'
	
	# order list using the object attribute
	# ordering = ['-date']
	
	# records per page
	paginate_by = 7

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Exprecord.objects.filter(contributor=user).order_by('-date')


# class ExprecordDetailView(DetailView):
# 	# <app>/<model>_detail.html --> template naming convention
# 	model = Exprecord

class ExprecordCreateView(LoginRequiredMixin, CreateView):
	# <app>/<model>_form.html --> template naming convention
	model = Exprecord
	fields = ['item', 'project', 'date', 'cost', 'proof']

	# IntegrityError at /exprecord/new/
	# null value in column "contributor_id" violates not-null constraint
	# no contributor specified for the exprecord
	# provide contributor to the form instance by overriding 'form_valid()' and
	# then run 'form_valid()' with the form data
	def form_valid(self, form):
		messages.success(self.request, f'Expense record created successfully!')
		form.instance.contributor = self.request.user
		return super().form_valid(form)

# class ExprecordUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
# 	# <app>/<model>_form.html --> template naming convention
# 	model = Exprecord
# 	fields = ['item', 'project', 'date', 'cost', 'proof']

# 	# IntegrityError at /post/new/
# 	# null value in column "contributor_id" violates not-null constraint
# 	# no contributor specified for the exprecord
# 	# provide contributor to the form instance by overriding 'form_valid()' and
# 	# then run 'form_valid()' with the form data
# 	def form_valid(self, form):
# 		form.instance.contributor = self.request.user
# 		return super().form_valid(form)

# 	# to ensure that only the user who created a post can update that post
# 	def test_func(self):
# 		exprecord = self.get_object()
# 		if self.request.user == exprecord.contributor:
# 			return True
# 		return False



# class ExprecordDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
# 	# <app>/<model>_confirm_delete.html --> template naming convention
# 	model = Exprecord

# 	# ImproperlyConfigured at /exprecord/10/delete/
# 	# No URL to redirect to. Provide a success_url.
# 	success_url = '/exprecords/'

# 	# to ensure that only the user who created a exprecord can update that exprecord
# 	def test_func(self):
# 		exprecord = self.get_object()
# 		if self.request.user == exprecord.contributor:
# 			return True
# 		return False


def about(request):
	context = {
		'title': 'About'
	}
	return render(request, 'exprecords/about.html', context)