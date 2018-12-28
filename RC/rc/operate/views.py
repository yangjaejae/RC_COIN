from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse

import requests

from info.models import Notice
from board.models import Comment
from django.contrib.auth.models import User

import json
# Create your views here.

def dashboard(request):
    context = {}
    context['notice_list'] = get_notices()
    context['comment_cnt'] = get_comment_cnt()
    context['account_cnt'] = get_account_cnt()
    context['tx_cnt']      = get_tx_cnt()
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

def get_comment_cnt():
    comment = Comment.objects.all()
    comment_cnt = len(comment)
    return comment_cnt

def get_account_cnt():
    users = User.objects.all()
    user_cnt = len(users)
    return user_cnt

def get_tx_cnt():
    tx_height = 0
    get_block_url = "http://192.168.0.28:3000/get_tx_cnt"
    try:
        response = requests.get(get_block_url)
        json_format = json.loads(response.text)
        tx_height = json_format['block_height']
    except Exception as e:
        print(e)
    return tx_height