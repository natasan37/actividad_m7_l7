from django.http import HttpResponse

def home(request):
    html = """
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f4f7f6; }
        .container { text-align: center; padding: 40px; background: white; border-radius: 10px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); }
        h1 { color: #2c3e50; margin-bottom: 10px; }
        p { color: #7f8c8d; margin-bottom: 25px; }
        a { display: inline-block; padding: 10px 20px; background-color: #3498db; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; }
        a:hover { background-color: #2980b9; }
    </style>
    <div class="container">
        <h1>MediMatch</h1>
        <p>Sistema administrativo en línea.</p>
        <a href='/admin/'>Acceder al Panel de Administración</a>
    </div>
    """
    return HttpResponse(html)
