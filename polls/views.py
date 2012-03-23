# -*- coding: utf-8 -*-

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required

from pythontr_org.polls.models import Choice, Poll, Vote

from django.core.exceptions import ValidationError


def index(request):
    """
        Son 5 anketi listelemek için kullanılır.
    """
    
    latest_poll_list = Poll.objects.all()[:5]
    return render(request, 'polls/index.html', locals())


def detail(request, poll_id):
    """
        Anket detaylarını göstermek için kullanılır.
    """
    
    poll = get_object_or_404(Poll, pk=poll_id)    
    return render(request, 'polls/detail.html', locals())


def results(request, poll_id):
    """
        Anket sonuçlarını göstermek için kullanılır.
    """
    
    poll = get_object_or_404(Poll, pk=poll_id)    
    return render(request, 'polls/results.html', locals())

@login_required
def vote(request, poll_id):
    """
        Ankete oy vermek için kullanılır.
    """
    
    poll = get_object_or_404(Poll, pk=poll_id)
    
    try:
        selected_choice = poll.choice_set.get(pk=request.POST['choice'])
        vote = Vote(user=request.user, poll=poll, choice=Choice.objects.get(pk=request.POST['choice']))
        vote.save()
        
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the poll voting form.
        
        error_message = u'Bir seçeneği seçmediniz.'
        
        return render(request, 'polls/detail.html', locals())
    
    except ValidationError:
        error_message = u'Bu ankete zaten oy kullanmışsınız.'
        
        return render(request, 'polls/detail.html', locals())
    
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        
        return redirect('polls:results', poll_id)