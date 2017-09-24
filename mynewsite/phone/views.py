#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Phonelist

# Create your views here.
def listting(request):
    html = '''
<!DOCTYPE html>
<html>
<head>
<meta  charset='utf-8'>
<title>中古手机列表</title>
</head>
<body>
<h2>以下是目前本店销售中的二手手机列表</h2>
<table width=400 border=1 bgcolor='#ccffcc'>
{}
</table>
</body>
'''
    products = Phonelist.objects.all()
    tags = '<tr><td>产品</td><td>售价</td><td>库存量</td></tr>'
    for p in products:
        tags = tags + '<tr><td>{}</td>'.format(p.name)
        tags = tags + '<td>{}</td>'.format(p.price)
        tags = tags + '<td>{}</tr>'.format(p.qty)
    return HttpResponse(html.format(tags))
