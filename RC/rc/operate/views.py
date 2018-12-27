from django.shortcuts import render

from info.models import Notice
# Create your views here.
def dashboard(request):
    
    context = {}
    context['notice_list'] = get_notices()
    return render(request, 'operate/manage_dashboard.html', (context))

def users(request):
    return render(request, 'operate/manage_users.html', ({}))

def approval(request):
    return render(request, 'operate/manage_approval.html', ({}))

def notice(request):
    return render(request, 'operate/manage_notice.html', ({}))

def tables(request):
    return render(request, 'operate/manage_tables.html', ({}))

def comments(request):
    return render(request, 'operate/manage_comments.html', ({}))

## utils
def check_length(string, max_len):
    result = ""
    if len(string) > max_len:
        result = str(string)[0:max_len] + "..."
    else:
        result = str(string)
    return result

## query
def get_notices():
    notice = Notice.objects.order_by('-id')
    notice_list = []
    for li in list(notice)[0:4]:
        temp = {}
        temp['id'] = li.id
        temp['title'] = check_length(str(li.title), 5)
        temp['writer'] = check_length(str(li.writer), 5)
        temp['status'] = li.status
        temp['create_date'] = str(li.create_date)[0:10]
        temp['modify_date'] = str(li.modify_date)[0:10]
        notice_list.append(temp)
    return notice_list