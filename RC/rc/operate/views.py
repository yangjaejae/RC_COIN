from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.views.generic import ListView, DetailView, View,TemplateView

import requests

from info.models import Notice
from board.models import Comment, BoardLiker
from store.models import Photo, Store
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from rest_framework.views import APIView
from rest_framework.response import Response

import json

Userchart = get_user_model()

# Create your views here.
def main(request):
    return render(request, 'operate/manage_main.html', ({}))

def dashboard(request):
    context = {}
    context['notice_list']         = get_notices()
    context['publish']       = get_publish_amount()
    context['account_cnt']         = get_account_cnt()
    context['tx_cnt']              = get_tx_cnt()
    context['store_cnt']           = get_store_cnt()
    context['store_waiting_list']  = get_waiting_store()
    return render(request, 'operate/manage_dashboard.html', (context))

#--------------------------------------사용자관리-----------------------------------------------#
class usersMyLV(TemplateView):
    paginate_by = 5
    # context_object_name = 'users'
    template_name = 'operate/manage_users.html'

    def get_context_data(self, **kwargs):
        
        context = super(usersMyLV, self).get_context_data(**kwargs)
        
        username = self.request.GET.get('keyword', '')
        context['users'] = User.objects.filter(username__icontains=username).order_by('-id')
        
        # if username:
        return context

def get_like(request):
    user_id = request.GET.get('user_id', '')
    like = BoardLiker.objects.filter(liker = user_id)
    board = BoardLiker.objects.filter(board = user_id)
       
    context = {}
    context['like_cnt'] = len(like)
    context['board_cnt'] = len(board)
    json_format = json.dumps(context)
    return HttpResponse(json_format, content_type="application/json:charset=UTF-8") 
#-------------------------------------------------------------------------------------------#

#--------------------------------------가맹점승인관리-----------------------------------------------#
class ApprovalLV(TemplateView):
    paginate_by = 5
    template_name = 'operate/manage_approval.html'

    def get_context_data(self, **kwargs):
        context = super(ApprovalLV, self).get_context_data(**kwargs)
        context['stores'] = Photo.objects.filter(store__status='w')
        return context

def get_approval(request):

    print(request.GET.get('store_id'))
    store_id = request.GET.get('store_id', '')
    store = get_object_or_404(Store, id=store_id)
    context = {}
    if store.status == 'w':
        store.status = 'a'
        store.save()
        context['result'] = 'y'
    else:
        context['result'] = 'n'

    json_format = json.dumps(context)
    return HttpResponse(json_format, content_type="application/json:charset=UTF-8") 
#-------------------------------------------------------------------------------------------#

#--------------------------------------공지사항관리-----------------------------------------------#

def notice(request):
    return render(request, 'operate/manage_notice.html', ({}))

#--------------------------------------발행이력관리-----------------------------------------------#
def publish(request):
    context = {}
    publish_list = []
    publish_list = list(get_publish_amount()['publish_list'])
    context['publish_list'] = publish_list
    return render(request, 'operate/manage_publish.html', (context))
#-------------------------------------------------------------------------------------------#

def discount_rate(request):
    return render(request, 'operate/manage_discount_rate.html', ({}))

def network(request):
    return render(request, 'operate/manage_network.html', ({}))


##----------------------차트관리------------------------------------------------#

class ChartHomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'operate/manage_statistics.html', {"customers": 10})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        # qs_count = User.objects.all().count()
        labels = ["사용자", "숙박", "레저", "음식"]
        labels_second = ['10대', '20대','30대','40대','50대','60대']
        default_items = [70, 45, 35, 25]
        default1_items = [70, 20 ,20, 10, 15,5]
        data = {
                "labels": labels,
                "default": default_items,
                "labels_second" : labels_second,
                "default1": default1_items,
        }
        return Response(data)

#################region############################################
class regional(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'operate/manage_statistics_regional.html', {"customers": 10})


##################gender#########################################
class gender(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'operate/manage_statistics_gender.html', {"customers": 10})
##################store#########################################
class store(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'operate/manage_statistics_store.html', {"customers": 10})

#-----------------------------------------------------------------------#



def login_required(request):
    return render(request, 'redirect/manage_login_require.html', ({}))

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

def get_publish_amount():
    get_publish_url = "http://127.0.0.1:3000/get_total_publish"
    publish_data = {}
    publish_amount = 0

    try:
        response = requests.get(get_publish_url)
        json_format = json.loads(response.text)
        print(type(json_format))
        data_list = []
        for datas in json_format:
            data = {}
            publish_amount = datas['balance']
            data['tx_id'] = check_length(str(datas['tx_id']),7)
            data['amount'] = datas['amount']
            data['person'] = datas['trader']
            data['date'] = datas['date']
            data_list.append(data)
            
        publish_data['total_publish'] = publish_amount
        publish_data['publish_list'] = data_list
    except Exception as e:
        print(e)
    return publish_data

def get_account_cnt():
    users = User.objects.all()
    user_cnt = len(users)
    return user_cnt

def get_tx_cnt():
    tx_height = 0
    get_block_url = "http://127.0.0.1:3000/get_tx_cnt"
    try:
        response = requests.get(get_block_url)
        json_format = json.loads(response.text)
        tx_height = json_format['block_height']
    except Exception as e:
        print(e)
    return tx_height

def get_store_cnt():
    store = Store.objects.all()
    store_cnt = len(store)
    return store_cnt

def get_waiting_store():
    store = Store.objects.filter(status='w').order_by('-modified_date')[0:4]
    store_list = []
    for li in store:
        stores = {}
        stores['name'] = li.name
        stores['modified_date'] = li.modified_date
        stores['corporate_number'] = li.corporate_number
        if str(li.category).strip() == "쇼핑":
            stores['category'] = 1
        if str(li.category).strip() == "레저":
            stores['category'] = 2
        if str(li.category).strip() == "숙박업":
            stores['category'] = 3
        if str(li.category).strip() == "요식업":
            stores['category'] = 4
        store_list.append(stores)
    print(store_list)
    return store_list
