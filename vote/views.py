from django.shortcuts import render
from django.shortcuts import *
from .models import *
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import *
from forms import *
from django.core.context_processors import *
from datetime import datetime


def votes(request):
    vote_form = VoteForm
    args = {}
    args.update(csrf(request))
    args['votes'] = Vote.objects.all()
    args['form'] = vote_form
    return render_to_response('vote/votes.html', args)


def vote(request, vote_id):
    return render_to_response('vote/vote.html', {'vote': Vote.objects.get(id=vote_id),
                                                 'answers': Answer.objects.filter(answer_vote_id=vote_id)})


def addanswer(request, description_id=1):
    try:
        if description_id in request.COOKIES:
            redirect('/')
        else:
            answer = Answer.objects.get(id=description_id)
            answer.count += 1
            answer.save()
            response = redirect('/')
            response.set_cookie(description_id, "test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect("/")


def addvote(request):
    if request.POST:
        form = VoteForm(request.POST)
        if form.is_valid():
            args = {}
            args.update(csrf(request))
            vote = form.save(commit=False)
            vote.date = datetime.now()
            form.save()
            args['vote'] = vote
            args['answers']=Answer.objects.filter(answer_vote=vote)
    return render_to_response('vote/addanswers.html', args)

def addanswers(request, id_v=1):
    if request.POST:
        form = AnswerForm(request.POST)
        if form.is_valid():
            args = {}
            args.update(csrf(request))
            answer = form.save(commit=False)
            answer.count = 0
            answer.id_vote = id_v
            form.save()
            args['vote'] = Vote.objects.get(id=vote.id)
            args['votedescriptions']=Answer.objects.filter(id_vote=id_v)
    return render_to_response('vote/addanswers.html', args)




