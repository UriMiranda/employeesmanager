from django.http import HttpResponse

def main_view(request):
    html = '<html><body><h3>Employeer manager Magazine Luiza</h3><button href="/admin" role="link" onclick="startAdmin()">Abrir admin</button><script>function startAdmin(){window.open("/admin", "self")}</script></body></html>'
    return HttpResponse(html)