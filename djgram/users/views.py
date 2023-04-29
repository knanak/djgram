from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import SignUpForm

def main(request):
    if request.method=='GET':
        return render(request, 'users/main.html')
    elif request.method =='POST':
        username=request.POST['username']
        pwd=request.POST['pwd']
        user=authenticate(request, username=username, password=pwd)
    
        if user is not None :
            login(request, user)
            return HttpResponseRedirect(reverse('posts:index'))
        
        else :
            return render(request, 'users/main.html')
        
def signup(request):
    if request.method == 'GET':
        form=SignUpForm()
        return render(request, 'users/signup.html', {'form':form})
    
    elif request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():  ## form이 유효하지 않는 경우는 어떤 경우??
            form.save()

            # 회원가입 후 자동로그인
            # 1) db에서 데이터 가져오기
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(request, username=username, password=password)

            # 2) 로그인 로직
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('posts:index'))
        
        return render(request, 'users/main.html')