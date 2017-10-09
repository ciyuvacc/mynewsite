#coding:utf8
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template.loader import get_template
from .models import Phonelist

# Create your views here.
#def listting(request):
#    html = '''
#<!DOCTYPE html>
#<html>
#<head>
#<meta  charset='utf-8'>
#<title>中古手机列表</title>
#</head>
#<body>
#<h2>以下是目前本店销售中的二手手机列表</h2>
#<table width=400 border=1 bgcolor='#ccffcc'>
#{}
#</table>
#</body>
#'''
#    products = Phonelist.objects.all()
#    tags = '<tr><td>产品</td><td>售价</td><td>库存量</td></tr>'
#    for p in products:
#        tags = tags + '<tr><td>{}</td>'.format(p.name)
#        tags = tags + '<td>{}</td>'.format(p.price)
#        tags = tags + '<td>{}</tr>'.format(p.qty)
#    return HttpResponse(html.format(tags))




def listting(request):
    products = Phonelist.objects.all()
    template = get_template('list.html')
    html =  template.render({'products':products})
    return HttpResponse(html)

#def disp_detail(request,sku):
#    html = '''
#<!DOCTYPE html>
#<html>
#<head>
#<meta  charset='utf-8'>
#<title>{}</title>
#</head>
#<body>
#<h2>{}</h2>
#<hr>
#<table width=400 border=1 bgcolor='#ccffcc'>
#{}
#</table>
#<a href='/list'>返回列表</a>
#</body>
#</html>
#'''
#    try:
#        p = Phonelist.objects.get(sku=sku)
#    except Phonelist.DoesNotExist:
#        raise Http404('找不到指定的产品编号')
#    tags = '<tr><td>产品编号</td><td>{}</td></tr>'.format(p.sku)
#    tags = tags + '<tr><td>产品名称</td><td>{}</td></tr>'.format(p.name)
#    tags = tags + '<tr><td>二手价格</td><td>{}</td></tr>'.format(p.price)
#    tags = tags + '<tr><td>库存数量</td><td>{}</td></tr>'.format(p.qty)
#    #return HttpResponse(html.format(p.sku,p.name,tags))
#    return HttpResponse(html.format(p.sku,p.name,tags))





#def disp_detail(request,sku):
#    try:
#        p = Phonelist.objects.get(sku=sku)
#    except Phonelist.DoesNotExist:
#        raise Http404('找不到指定的产品编号')
#    tags = '<tr><td>产品编号</td><td>{}</td></tr>'.format(p.sku)
#    tags = tags + '<tr><td>产品名称</td><td>{}</td></tr>'.format(p.name)
#    tags = tags + '<tr><td>二手价格</td><td>{}</td></tr>'.format(p.price)
#    tags = tags + '<tr><td>库存数量</td><td>{}</td></tr>'.format(p.qty)
#    template = get_template('disp.html')
#    html = template.render({'pname':p.name,'tags':tags})
#    return HttpResponse(html)




def disp_detail(request,sku):
    try:
        p = Phonelist.objects.get(sku=sku)
    except Phonelist.DoesNotExist:
        raise Http404('找不到指定的产品编号')
    template = get_template('disp.html')
    html = template.render({'product':p})
  
    return HttpResponse(html)


def index(request):
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)
