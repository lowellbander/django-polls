# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext, loader
from polls.models import Poll

def index(request): # takes an HTTP Request (verb(?)) as an argument
	latest_poll_list = Poll.objects.order_by('-pub_date')[:5] # first five
	# latest_polls_list = Poll.objects.all()
	# output = ', '.join([p.question for p in latest_polls_list])
	template = loader.get_template('polls/index.html')
	context = RequestContext(request, {
		'latest_poll_list' : latest_poll_list,
	})
	# return HttpResponse("asdasd")
	return HttpResponse(template.render(context))

def detail(request, poll_id):
	return HttpResponse('You\'re looking at poll %s.' % poll_id)

def results(request, poll_id):
	return HttpResponse('You\'re looking at the results of poll %s.' % poll_id)

def vote(request, poll_id):
	return HttpResponse('You\'re voting on poll %s.' % poll_id)