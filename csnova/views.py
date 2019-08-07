from django.shortcuts import render

# Create your views here.

def student(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'csnova/student/project.html')
def teacher(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    return render(request, 'csnova/teacher/project.html')
