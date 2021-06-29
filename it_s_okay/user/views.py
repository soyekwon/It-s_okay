from django.shortcuts import render, redirect
from django.contrib.auth.hashers import check_password
from .models import Normaluser
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
#pw 변경을 위해 line 6~8까지 세줄 추가하였습니다.


# 회원가입 대안버전

# @csrf_exempt 
# def register(request):
#     if request.method == "POST":
#         if request.POST["password"] == request.POST["re_password"]:
#             normaluser = Normaluser.objects.create_user(
#                 username=request.POST["username"],password=request.POST["password"]
#             )
#             auth.login(request, normaluser)
#             return redirect('user/login.html')
#         return render(request, 'user/register.html')
#     return render(request, 'user/register.html')


#회원가입 초기버전 

@csrf_exempt 
def register(request):
    if request.method == 'GET':
        return render(request, 'user/register.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        re_password = request.POST['re_password']

        res_data = {}

        if not (username and password and re_password):
            res_data['error'] = "모든 값을 입력해야합니다."
        elif password != re_password:
            res_data['error'] = '비밀번호가 일치하지 않습니다'
        else:
            normaluser = Normaluser.objects.create_user(
                username=username,
                password=password
            )

            normaluser.save()
            return render(request, 'main/home.html', res_data)


    return render(request, 'user/register.html', res_data)

# # 로그인 대안버전

@csrf_exempt 
def login(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        normaluser = auth.authenticate(request, username=username, password=password)
        
        if normaluser is not None:
            auth.login(request, normaluser)
            return redirect('/')
        else:
            return render(request, 'user/login.html', {'error':'아이디 혹은 비밀번호가 다릅니다.'})

    else:
        return render(request, 'user/login.html')

# 로그인 초기버전

# @csrf_exempt 
# def login(request):
#     if request.method == 'GET':
#         return render(request, 'user/login.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username', None)
#         password = request.POST.get('password', None)

#         res_data = {}
#         if not(username and password):
#             res_data['error'] = '모든 값을 입력해야합니다.'
#         else:
#             normaluser = Normaluser.objects.get(username=username)
#             if check_password(password, normaluser.password):
#                 request.session['user'] = normaluser.id
#                 return redirect('/')

#             else:
#                 res_data['error'] = '비밀번호를 틀렸습니다.'
        
#         return render(request, 'user/login.html', res_data)

def logout(request):
    if request.session.get('user'):
        del(request.session['user'])

        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')

def mypage(request):
    return render(request, "user/mypage.html")

# 비밀번호 변경 구현을 위한 코드
def change_pw(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('change_pw')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'user/change_pw.html', {
        'form': form
    })

# 회원 탈퇴를 위한 코드
def userDelete(request):
    user = request.user
    user.delete()
    logout(request)
    context = {}
    return render(request, 'user/farewell.html', context)



def signout(request):
    return render(request, 'user/signout.html')
