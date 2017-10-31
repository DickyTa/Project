from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views import generic

from .models import User, Student, Tutor, Wallet, Booked_session
# Create your views here.

def s_detail(request, s_id):
    u = User.objects.get(user_id = s_id)
    s = Student.objects.get(student_id = u)
    context = {'s': s}
    return render(request, 'polls/s_detail.html',context)

def t_detail(request, t_id):
    u = User.objects.get(user_id = t_id)
    t = Tutor.objects.get(tutor_id = u)
    context = {'t': t}
    return render(request, 'polls/t_detail.html',context)

def t_list(request):
    tutor_list = Tutor.objects.order_by('name')
    context = {'tutor_list': tutor_list}
    return render(request, 'polls/list.html', context)

def t_sort(request):
    tutor_list = Tutor.objects.order_by('-rating')
    context = {'tutor_list': tutor_list}
    return render(request, 'polls/list.html', context)

def t_search(request,search):
    tutor_list = Tutor.objects.filter(subject_tag = search)
    context = {'tutor_list': tutor_list}
    return render(request, 'polls/list.html', context)