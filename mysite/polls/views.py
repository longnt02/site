# Create your views here.
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from .models import Choice, Question
from django.utils import timezone
from django.template.response import TemplateResponse
from django.views import View
from django.http import HttpResponse
from django.template.loader import get_template

class IndexView(View):
    latest_question_list = Question.objects.filter(
        pub_date__lte=timezone.now()
    ).order_by('-pub_date')[:5]

    def get(self, request):
        template = get_template('polls/index.html')
        context = {'latest_question_list': self.latest_question_list}
        output = template.render(context, request)
        return HttpResponse(output)

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return TemplateResponse(request, 'polls/results.html', {'question': question})
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        context = {
            'question': question,
            'error_message': "You didn't select a choice.",
        }
        return TemplateResponse(request, 'polls/detail.html', context)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))