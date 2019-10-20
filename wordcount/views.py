import operator

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def count(request,):
    fullText = request.GET['fullText']

    wordlist = fullText.split()
    worddictionary = {}
    for word in wordlist:
        if word in worddictionary:
            worddictionary[word] += 1
        else:
            worddictionary[word] = 1
        
    sortedWords = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fullText': fullText, 'count': len(wordlist) , 'sortedWords' : sortedWords} )

def about(request):
    return render(request,'about.html')