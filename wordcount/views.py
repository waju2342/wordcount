
from django.http import  HttpResponse
from django.shortcuts import  render
import  operator

def homepage(request):
    return render( request, 'home.html')


def count(request):
    data = request.GET['fulltestarea']
    list_word = data.split()
    list_len = len(list_word)
    word_dict = {}
    for i in list_word:
        if i in word_dict:
            word_dict[i]+=1
        else:
            word_dict[i]=1
    sorted_list = sorted(word_dict.items(),key=operator.itemgetter(1),  reverse=True)

    return  render(request, 'count.html', { 'fulltext': data, 'total_word': list_len , 'words_dict':sorted_list })


def About(request):
    return  render (request, 'About.html')

