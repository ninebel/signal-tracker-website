from .. import * # Import from the __init__.py all (*) the necesary imports!

def view(request):
    
    return render_template('panel/panel.html', page='panel') 