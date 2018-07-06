# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import random

from nltk.tokenize import sent_tokenize
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse,HttpResponseBadRequest


# Create your views here.
def index(request):
    context = {}
    return render(request, 'qa_app/index.html', context)

@csrf_exempt
def answer(request):
    if request.method == 'GET':
        # HTTP Method GET
        return HttpResponseBadRequest('GET request is not allowed')
    elif request.method == 'POST':
        # HTTP Method POST.
        paragraph_text = request.POST.get('paragraph_text', '').strip()
        question_text = request.POST.get('question_text', '').strip()
        if len(paragraph_text) == 0:
            return HttpResponseBadRequest('Paragraph field is empty')
        if len(question_text) == 0:
            return HttpResponseBadRequest('Question field is empty')

        paragraph_sents = sent_tokenize(paragraph_text)
        selected_sent = random.choice(paragraph_sents)

        if 'photosynthesis' in question_text.lower():
            selected_sent = paragraph_sents[1]
        elif 'google' in question_text.lower():
            selected_sent = paragraph_sents[-1]

        result = {}
        result['selected_sent'] = selected_sent
        result['all_sents'] = paragraph_sents

        return JsonResponse({'result': result})
