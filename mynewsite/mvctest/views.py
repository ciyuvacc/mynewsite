from django.shortcuts import render

from django.http import HttpResponse

def about(request):
    html = '''
<!DOCTYPE html>
<html>
<head><title> About Myself</title></head>
<body>
<h2>Min-Huang Ho</h2>
<hr>
<p>
Hi, I am Min-Huang Ho,Nice to meet you!
</p>
</body>
</html>
'''
    return HttpResponse(html)
