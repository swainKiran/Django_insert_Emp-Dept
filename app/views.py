from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from app.models import Dept, Emp

def dept_display(request):
    if request.method == 'POST':
        id = request.POST["id"]
        nm = request.POST["nm"]
        loc = request.POST["loc"]
        
        DO = Dept.objects.get_or_create(deptid=id, deptname=nm, deptloc=loc)[0]
        DO.save()
        return HttpResponse('sucessfully added')
        return render(request, 'insert_dept.html')

def emp_display(request):
    QLDO = Dept.objects.all()
    QLEO = Emp.objects.all()
    if request.method == 'POST':
        eid = request.POST.get("eid")
        nm = request.POST.get("nm")
        sal = request.POST.get("sal")
        jb = request.POST.get("jb")
        hd = request.POST.get("hd")
        mgr = request.POST.get("mgr")
        cm = request.POST.get("cm", None)
        di = request.POST.get("di")

        DI = Dept.objects.get(deptid=di)
        WE = None if mgr == "none" else Emp.objects.get(emp_id=mgr)
        EO = Emp.objects.get_or_create(emp_id=eid, emp_name=nm, emp_sal=sal, job=jb, hire_date=hd, mgr=WE, coomition=cm, deptid=DI)[0]    
        EO.save()
        return HttpResponse('sucessfully added')

    d = {'QLDO': QLDO, 'QLEO': QLEO}
    return render(request, 'insert_emp.html', d)

def select_multiple(request):
     QLDO = Dept.objects.all()
     d = {'QLDO': QLDO}
     if request.method == 'POST':
        STL=request.POST.getlist('id')
        WOS=Emp.objects.none()
        for t in STL:
            WOS=WOS|Emp.objects.filter(deptid=t)
        d1={'WOS':WOS} 
        return render(request,'display_emp.html', d1) 

     return render(request,'select_multiple.html', d)
   
def checkBox(request):
    QLTO=Dept.objects.all()
    d={'QLTO':QLTO}
    return render(request,'checkBox.html',d)   