from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from random import randint
from django.template import loader
from rps_game.models import UserSelection, Status
from django.urls import reverse

# Create your views here.
ai = None
def index(request):
    n = 1
    defaultSelection = UserSelection.objects.get(id=n)
    win_lose = Status.objects.get(id=n)

    context = {
        'selection':defaultSelection,
        'state': win_lose,
        }

    template = loader.get_template('index.html')
    return HttpResponse(template.render(context))


def rock(request):
    user = UserSelection.objects.get(id=1)
    user.selection = "Rock"
    user.save()
    return HttpResponseRedirect(reverse('index'))

def paper(request):
    user = UserSelection.objects.get(id=1)
    user.selection = "Paper"
    user.save()
    return HttpResponseRedirect(reverse('index'))

def scissors(requet):
    user = UserSelection.objects.get(id=1)
    user.selection = "Scissors"
    user.save()
    return HttpResponseRedirect(reverse('index'))

def play(request):
    choices = ['Rock', 'Paper', 'Scissors']
    randChoices = []
    for i in range(15):
        randChoices.append(choices[randint(0,2)])

    try:
        computer = randChoices[randint(0, len(randChoices))]
    except IndexError:
        computer = randChoices[0]
        
    comp = UserSelection.objects.get(id=1)
    comp.computerSelection = computer
    comp.save()

    user = UserSelection.objects.get(id=1)

    # 0 Rock | 1 Paper | 2 Scissors
    def check(user, computer, choices):
        status = Status.objects.get(id=1)

        if user == choices[0] and computer == choices[1]:
            status.stat = "You Lose"
            status.outof += 1
            status.save()

        elif user == choices[0] and computer == choices[2]:
            status.stat = "You Win"
            status.score += 1
            status.save()

        elif user == choices[1] and computer == choices[0]:
            status.stat = "You Win"
            status.score += 1
            status.save()

        elif user == choices[1] and computer == choices[2]:
            status.stat = "You Lose"
            status.outof += 1
            status.save()

        elif user == choices[2] and computer == choices[0]:
            status.stat = "You Lose"
            status.outof += 1
            status.save()

        elif user == choices[2] and computer == choices[1]:
            status.stat = "You Win"
            status.score += 1
            status.save()
        elif user == computer:
            status.stat = "It's a tie"
            status.save()
        else:
            pass

    check(user.selection, user.computerSelection, choices)


    return(HttpResponseRedirect(reverse(index)))

def reset(request):
    default = UserSelection.objects.get(id=1)
    default.selection = "Select"
    default.save()

    default = Status.objects.get(id=1)
    default.stat = ""
    default.save()

    default = Status.objects.get(id=1)
    default.score = 0
    default.save()
    default.outof = 0
    default.save()

    return HttpResponseRedirect(reverse(index))
