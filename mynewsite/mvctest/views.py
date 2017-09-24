#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template.loader import get_template
import random
#
#def about(request):
#    html = '''
#<!DOCTYPE html>
#<html>
#<head><title> About Myself</title></head>
#<body>
#<h2>Min-Huang Ho</h2>
#<hr>
#<p>
#Hi, I am Min-Huang Ho,Nice to meet you!
#</p>
#</body>
#</html>
#'''
#    return HttpResponse(html)

def about(requtest):
    template = get_template('about.html')
    quotes = [ '永远不要向任何人解释你自己。因为喜欢你的人不需要，而不喜欢你的人不会相信.',
    '别让某人成为你生命中的优先，当你只是他们生命中的一个选择时。人与人之间的关系只有在彼此达到平衡时，运作的最恰当.',
    '生活不是单行线，一条路走不通，你可以转弯.',
    '让梦想成真的最好办法就是醒来.']
    html = template.render({'quote':random.choice(quotes)})
    return HttpResponse(html)
