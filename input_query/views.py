# -*- coding:utf-8 -*-
from django.shortcuts import render
from .forms import QueryForm
from .models import Hotel

import word2vec
import os
import nltk

vectorPath = './vectors.bin'
model = word2vec.load(vectorPath)
inputList = ''

def cosDistance(query, n):
    indexes, metrics = model.cosine(query, n)
    return model.generate_response(indexes, metrics).tolist()

def analogy(q_pos, q_neg, q_n):
    indexes, metrics = model.analogy(q_pos, q_neg, q_n)
    return model.generate_response(indexes, metrics).tolist()

def search(query):
    query = query.split(' ')
    for i in range(len(query)):
        query[i] = str(query[i])
        if query[i].isdigit():
            query[i] += ":"
    try:    
        q = analogy(query, [], 100)
        re = []
        for i in q:
            if ":" in i[0]:
                re.append(str(i[0][:-1]))
    except:
        pass
    return re
                
def get_query(request):
    return render(request, 'home.html', {})

def show(request):
    if request.method == 'POST':
        form = QueryForm(request.POST)
        if form.is_valid():
            local_content = form.data.get("content")
            
            # q是處理完的query後，留下來要查詢database的id
            q = search(local_content)
            
            hotel = []
            for h_id in q:
                try:
                    tmp = Hotel.objects.get(hotel_id=h_id)
                    tmp.comment = tmp.comment.replace("<", "[")
                    tmp.comment = tmp.comment.replace(">", "] ")
                    tmp.comment = tmp.comment.replace("\n", '<br>')
                    hotel.append(tmp)
                except:
                    continue
            return render(request, 'show.html', {'hotel':hotel, 'local_content':local_content})
        else:
            return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})
