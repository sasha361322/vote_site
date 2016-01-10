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


def addanswer(request, vote_id=1,answer_id=1):
    try:
        if vote_id in request.COOKIES:
            redirect('/')
        else:
            answer = Answer.objects.get(id=answer_id)
            answer.count += 1
            answer.save()
            response = redirect('/vote/get/%s/' % Answer.objects.get(id=answer_id).answer_vote_id)
            response.set_cookie(vote_id, "test")
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
            answer_form = AnswerForm
            args['form']=answer_form
    return render_to_response('vote/addanswers.html', args)

def addanswers(request, vote_id=1):
    if request.POST:
        form = AnswerForm(request.POST)
        if form.is_valid():
            args = {}
            args.update(csrf(request))
            answer = form.save(commit=False)
            answer.count = 0
            answer.answer_vote_id = vote_id
            form.save()
            args['vote'] = Vote.objects.get(id=vote_id)
            answer_form = AnswerForm
            args['form']=answer_form
            args['answers']=Answer.objects.filter(answer_vote_id=vote_id)
    return render_to_response('vote/addanswers.html', args)




