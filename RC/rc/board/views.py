from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from member.models import Profile

import json

from board.models import Board, Comment, BoardLiker
from board.forms import BoardForm

import datetime
from datetime import datetime as dt
# Create your views here.

class BoardLV(ListView):
    model = Board
    context_object_name = 'boards'
    paginate_by = 5

    def __init__(self):
        self.user_type = '1'

    def get_queryset(self):
        if self.request.user.username == '':
            queryset = Board.objects.filter(category=1)
        else:
            user = get_object_or_404(User, username=self.request.user.username)

            self.user_type = user.profile.type
            queryset = Board.objects.filter(writer__profile__type=self.user_type)
        return queryset

class BoardDV(DetailView):
    model = Board

    def __init__(self):
        self.add_cnt()

    def add_cnt(self):
        print(str(self.model))

    def get_context_data(self, **kwargs):
        context = super(BoardDV, self).get_context_data(**kwargs)

        added = self.object.count + 1
        board = get_object_or_404(Board, id=self.object.id)
        board.count = added
        board.save()

        comment_cnt = 0

        try:
            comment = get_object_or_404(Comment, board_id=self.object.id)
            comment_cnt = len(comment)
        except:
            comment_cnt = 0

        print()

        context['object'] = self.object
        context['comment_cnt'] = comment_cnt
        return context

def board_edit(request, board_id=None):

    user = request.user.pk

    if board_id:
        board = get_object_or_404(Board, pk=board_id)
    else:
        board = Board()

    if request.method == "POST":
        # POST 된 request 데이터를 가지고 Form 생성
        form = BoardForm(request.POST, instance=board)
        if form.is_valid():
            board = form.save(commit=False)
            board.board_id = Board(board_id)
            board.writer = User(user)
            board.save()
            # request 없이 페이지 이동만 한다.
        return redirect('board:list')
    else:
        # book instance에서 Form 생성
        form = BoardForm(instance=board)
        # 사용자의 request를 가지고 이동한다.
        return render(request, 'board/board_edit.html', dict(form=form, board=board))

def board_delete(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    board.delete()
    return redirect('board:list')

def get_comment(request):

    now = dt.now()

    board_id = request.GET.get('board_id', )

    comments = Comment.objects.filter(board_id=board_id)
    print(datetime.datetime.strptime(str(now),'%Y-%m-%d').strftime('%d/%m/%Y'))
    data_list = []
    for li in comments:
        print(now - datetime.datetime.strptime(str(li.modify_date),'%Y-%m-%d').strftime('%d/%m/%Y') )
        temp = {}
        temp['board_id'] = li.board_id.id
        temp['writer'] = str(li.writer.profile.user)
        temp['content'] = li.content
        temp['create_date'] = str(li.create_date)
        temp['modify_date'] = str(li.modify_date)
        temp['status'] = li.status
        data_list.append(temp)
    json_format = json.dumps(data_list)

    return HttpResponse(json_format, content_type="application/json:charset=UTF-8")

def chg_board(request):

    board_type = request.GET.get('board_type', )

    board = Board.objects.filter(writer__profile__type=board_type)

    data_list = []
    for li in board:
        temp = {}
        temp['id'] = li.id
        temp['title'] = li.title
        temp['content'] = li.content
        temp['count'] = li.count
        temp['recommend'] = li.recommend
        temp['writer'] = str(li.writer)
        temp['create_date'] = str(li.create_date)[0:10]
        temp['modify_date'] = str(li.modify_date)[0:10]
        temp['category'] = li.category
        temp['get_absolute_url'] = li.get_absolute_url()
        data_list.append(temp)
    json_format = json.dumps(data_list)

    return HttpResponse(json_format, content_type="application/json:charset=UTF-8")

def write_comment(request):
    board_id = request.GET.get('board_id', )
    input_comment = request.GET.get('comment', )
    user = request.user.pk

    comment = Comment()

    comment.board_id = Board(board_id)
    comment.writer = User(user)
    comment.content = input_comment
    comment.status = 'y'

    try:
        comment.save()

        result = json.dumps([
            {'result': 'seccess'}
        ])

    except Exception as e:
        print(e)
        result = json.dumps([
            {'result':'fail'}
        ])

    return HttpResponse(result, content_type="application/json:charset=UTF-8")

def add_like(request):
    board_id = request.GET.get('board_id', )
    user_type = request.user.profile.type
    liker = request.user.pk

    board = get_object_or_404(Board, pk=board_id)
    like = BoardLiker()

    if_liked = BoardLiker.objects.filter(liker=liker, board=board_id)

    if user_type != '1' and user_type != '2':
        result = json.dumps([
            {'likes': 'notLogin'}
        ])
        return HttpResponse(result, content_type="application/json:charset=UTF-8")
    elif if_liked:
        result = json.dumps([
            {'likes': 'already'}
        ])
        return HttpResponse(result, content_type="application/json:charset=UTF-8")
    else:
        like.liker = User(liker)
        like.board = board
        like.save()

        added = board.recommend + 1
        board.recommend = added
        board.save()
        result = json.dumps([
            {'likes' : added }
        ])
        return HttpResponse(result, content_type="application/json:charset=UTF-8")

def test(request):
    return render(request, "board/test.html", ({}))