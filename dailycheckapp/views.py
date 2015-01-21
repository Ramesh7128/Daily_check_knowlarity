from django.shortcuts import render
from models import Employee, Messages
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def get_employee_list(max_results=0, starts_with=''):
        profile_list = []
        if starts_with:
                users = User.objects.get(username=request.user)
                profile_list = Employee.objects.filter(name__istartswith=starts_with)

        if max_results > 0:
                if len(profile_list) > max_results:
                        profile_list = profile_list[:max_results]

        return profile_list



def index(request):
    context = RequestContext(request)

    context_dict = {}
    if request.method == 'GET':
        if request.user.is_authenticated():
            users = User.objects.get(username=request.user)
            emp_list = Employee.objects.filter(users=users)
            context_dict['profile_list'] = emp_list

        # context_dict['profile_list'] = profile_list


    return render_to_response('base.html', context_dict, context)


def addEmployees(request):
    context = RequestContext(request)
    context_dict = {}
    users = User.objects.get(username=request.user)

    if request.method=='POST':
        empl_name = request.POST.get('employeename')
        designation = request.POST.get('designation')
        phoneno = request.POST.get('phoneno')

        Employee.objects.create(users=users,name=empl_name,designation=designation,phoneno=phoneno)
        # personalprofile.objects.create(users=users, workex=workexp, stack1=stack1, point1=points1, stack2=stack2, point2=points2, stack3=stack3, point3=points3, stack4=stack4, point4 = points4)
        return HttpResponseRedirect('/')

    # context_dict['forms'] = form

    return render_to_response('addlinks.html', context_dict, context)


def employlist(request):
    context = RequestContext(request)
    starts_with=""
    context_dict = {}
    if request.method == 'GET':
        starts_with = request.GET['username']
    stud_list = get_employee_list(8, starts_with)
    context_dict['profile_list'] = stud_list
    return render_to_response('employeelist.html', context_dict, context)

@csrf_exempt
def emplpost(request):
    if request.method == "POST":
        post_file = request.POST.get('data1')
        post_file = str(post_file)
        empl_proile = Employee.objects.get(id=1)
        Messages.objects.create(employee=empl_proile, messages=post_file)
    return HttpResponseRedirect('/')


def emplprofile(request,userid):
    context = RequestContext(request)
    context_dict = {}
    empl_proile = Employee.objects.get(id=userid)
    context_dict['empl_proile'] = empl_proile
    try:
        messageslist = Messages.objects.all()
        context_dict['messageslist'] = messageslist
    except:
        pass
    return render_to_response('emplprofile.html', context_dict, context)





