from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.template import loader
from .forms import SignUpForm
from member.models import Profile


# Create your views here.

def myinfo_edit(request, type):
    if request.method == 'POST':

        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.age = form.cleaned_data.get('age')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.type = type
            user.profile.status = 'Y'
            user.save()

            msg = {
                'title': '회원가입',
                'text': '환영합니다. 메인페이지로 자동 이동합니다. 로그인을 해주세요.'
            }
            return render(request, 'registration/done.html', msg)

        else:
            user = get_object_or_404(User, username=request.user.username)
            profile = user.profile
            user.set_password(form.cleaned_data.get('password1'))
            user.email = form.cleaned_data.get('email')
            user.profile.age = form.cleaned_data.get('age')
            user.profile.gender = form.cleaned_data.get('gender')
            user.profile.type = form.cleaned_data.get('type')
            user.profile.status = form.cleaned_data.get('status')
            user.save()
            update_session_auth_hash(request, user)

            msg = {
                'title': '회원정보수정',
                'text': '정보가 수정되었습니다.메인페이지로 자동 이동합니다.'
            }
            return render(request, 'registration/done.html', msg)

    else:
        if type == 'A' or type == 'U' or type == 'S':
            form = SignUpForm()
            return render(request, 'registration/register.html', {'form': form})
        else:
            user = get_object_or_404(User, username=type)
            profile = user.profile

            info = {
                'username': user.username,
                'email': user.email,
                'age': profile.age,
                'gender': profile.gender,
                'type': profile.type,
                'status': profile.status
            }
            return render(request, "registration/register.html", info)


def doneView(request):
    template = 'registration/done.html'

    return render(request, template)
