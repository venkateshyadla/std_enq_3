from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from .models import Enquiry
from .forms import Enquiryform

offered={
            "Computer Science and Engineering":100000,
            "Artificial Intellegence and Machine Learning":120000,
            "Computer Science and Bussiness Systems":98000,
            "Information Technology":95000,
            "Electrical and Electronics Engineering":88000,
            "Electronics And Communication Engineering":87000
            }

def validation(form,request):
    if request.method == 'POST':
        duration = {'B.tech':4,'M.tech':2}
        name = request.POST.get('name')
        course = request.POST.get('course')
        branch = request.POST.get('branch')
        course = request.POST.get('course')
        father_name = request.POST.get('father_name')
        print("just entered.....!")
        if form.is_valid():
            std = form.save()
            std_id = std.pk
            mail = get_object_or_404(Enquiry,pk = std_id)
            email = mail.email # you can use email id also here but it's fine
            #data_jump = dict(email=email,std_id = std_id)
            fee = offered[branch]
            total_fee = 19800 + fee
            duration = duration[course]
            print("record inserted......!")
            data = {'s_name':name,'course':course,'branch':branch,'discounts':'yes','fee':fee,'duration':duration,'father_name':father_name,'std_id':std_id,'total_fee':total_fee}
            request.session['data_jump_1'] = email
            request.session['data_jump_2'] = std_id
            return data
    else:
        return False
    

def welcome(request):
    if request.method == 'POST':
        print("post post post")
        redirect(enq_view)
    return render(request,'welcome.html')

def enq_view(request):
    courses = ['B.tech','M.tech']
    branches = [branch for branch in offered.keys()]
    return render(request,'enq.html',{'courses':courses,'branches':branches})

def fee_fix_form_view(request):
    form = Enquiryform(request.POST)
    info = validation(form,request)
    if info is not False:
        return render(request,'fee_fix_form.html',info)
    else:
        print("give the values in proper format......!")
    return render(request,'fee_fix_form.html',info)
def success_view(request):
    alert = True
    if request.method == 'POST':
        if 'accepted' in request.POST:
            data_catch_1 = request.session.get('data_jump_1',None)
            data_catch_2 = request.session.get('data_jump_2',None)
            agree = request.POST.get('accepted')
            if agree == 'on'and data_catch_1 is not None:
                print("thakn you")
                data = {'email':data_catch_1,'std_id':data_catch_2}
                return render(request,'success.html',data)
        else:
            return render(request,'fee_fix_form.html',{'alert':alert})
            #return redirect(fee_fix_form_view,alert)

    return render(request,'fee_fix_form.html')
