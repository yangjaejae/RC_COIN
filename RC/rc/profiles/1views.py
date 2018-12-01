from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User, BaseUserManager
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.core.mail import send_mail
from .forms import ProfileForm
import json

# Create your views here.

def done(request):
    return render(request, 'registration/done.html')


def getContext(user_id):
    user = get_object_or_404(User, pk=user_id)
    context = {
        "username" : user.username,
        "email" : user.email,
        "image" : user.profile.image,
        "gender" : user.profile.gender,
        'birth_year': user.profile.birth_year,
        'birth_month': user.profile.birth_month,
        'birth_date': user.profile.birth_date,
        "type" : user.profile.type,
        "status" : user.profile.status
    }
    return context


def my_info(request, account_id=None):
    template_name = "registration/profile_myInfo.html"
    context = getContext(account_id)
    return render(request, template_name, context)


def account_edit(request, account_id=None):
    context = {}
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)

        if form.is_valid():
            user = form.save()
            context['title'] = '회원가입 완료'
            context['messages'] = ['환영합니다.', '메인화면으로 이동합니다.', '로그인을 해주세요.']
        else:
            user = get_object_or_404(User, pk=account_id)
            user.set_password(form.cleaned_data.get('password1'))
            user.email = form.cleaned_data.get('email')
            # update_session_auth_hash(request, user)
            context['title'] = '수정되었습니다.'
            context['messages'] = ['메인화면으로 이동합니다.', '다시 로그인을 해주세요.']

        user.profile.gender = form.cleaned_data.get('gender')
        user.profile.birth_year = form.cleaned_data.get('birth_year')
        user.profile.birth_month = form.cleaned_data.get('birth_month')
        user.profile.birth_date = form.cleaned_data.get('birth_date')
        user.save()
        return render(request, 'registration/done.html', context)
    else:
        if account_id:
            context = getContext(account_id)
            return render(request, 'registration/profile_register.html', context)
        else:
            form = ProfileForm()
            return render(request, 'registration/profile_register.html', { 'form' : form })


def search_username(request):
    if request.method == 'POST':
        user_list = User.objects.filter(email=request.POST.get("email"))
        context = { 'user_list' : user_list }
        if not user_list:
            context['error'] = '일치하는 회원정보가 없습니다.'
        return render(request, 'registration/search_username.html', context)

    return render(request, 'registration/search_username.html')


def check_username(request):
    username = request.GET.get('username', None)

    data = {
        'result': User.objects.filter(username=username).exists()
    }
    return JsonResponse(data)


def search_password(request):
    context = {}
    if request.method == 'POST':
        user = User.objects.filter(username=request.POST.get("username"), email=request.POST.get("email"))
        if user:
            new_pwd = BaseUserManager().make_random_password(length=10, allowed_chars='abcdefghjkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ23456789')
            # user[0].set_password(new_pwd)
            # user[0].save()
            # print(user[0])
            # print(new_pwd)
            # send_mail(
            #     '[RC: 발신전용] 비밀번호 안내 메일',
            #     '비밀번호가 [ ' + new_pwd + ' ]로 초기화 되었습니다.',
            #     'doradora46@naver.com',
            #     [user[0].email],
            #     fail_silently=False,
            # )
            context['title'] = '비밀번호 초기화'
            context['messages']= ['임시 비밀번호가 등록된 이메일로 발송 되었습니다.', '로그인 후, 비밀번호를 변경해 주세요.']
            return render(request, 'registration/done.html', context)
        else:
            context['error'] = '일치하는 회원정보가 없습니다.'

    return render(request, 'registration/search_password.html', context)


def check_password(request, account_id=None):
    context = {}
    if request.method == 'POST':
        user = request.user.check_password(request.POST.get('password'))
        if user:
            return redirect('profile:account_edit', account_id=account_id)
        else:
            context['error'] = '비밀번호가 일치하지 않습니다.'
    return render(request, 'registration/check_password.html', context)


# --- @login_required
class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)

