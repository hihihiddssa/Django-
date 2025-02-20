from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User, Drug
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404


# 注册方法
def register(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            try:
                User.objects.create_user(email=email, password=password)
                messages.success(request, 'Registration successful!')
                return redirect('login')
            except ValueError as e:
                messages.error(request, str(e))
        else:
            messages.error(request, 'Email and password are required.')
    return render(request, 'accounts/register.html')

# 登录方法
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        if email and password:
            user = authenticate(request, email=email, password=password)
            if user:
                login(request, user)
                messages.success(request, '登录成功！')
                request.session['is_logged_in'] = True
                return redirect('home')
            else:
                messages.error(request, '用户名或密码不正确。')
        else:
            messages.error(request, 'Email and password are required.')
    return render(request, 'accounts/login.html')

# 登出方法
def user_logout(request):
    if request.session.get('is_logged_in'):
        del request.session['is_logged_in']
    return redirect('login')

# home 页面（包含 session 验证）
@login_required
def home_view(request):
    #登录验证
    if not request.session.get('is_logged_in'):
        return redirect('login')
    user = request.user
    drugs = Drug.objects.all()

    # 处理查询请求
    search_query = request.GET.get('search')
    if search_query:
        drugs = drugs.filter(drug_name__icontains=search_query)

    return render(request, 'accounts/home.html', {'user': user, 'drugs': drugs})
# 添加药品
@login_required
def add_drug(request):
    #登录验证
    if not request.session.get('is_logged_in'):
        return redirect('login')
    if request.method == 'POST':
        name = request.POST.get('name')
        company = request.POST.get('company')
        quantity = request.POST.get('quantity')
        code = request.POST.get('code')
        Drug.objects.create(drug_name=name, drug_company=company, drug_quantity=quantity, drug_code=code)
        messages.success(request, '药品添加成功！')
        return redirect('home')
    return render(request, 'accounts/add_drug.html')

# 编辑药品
@login_required
def edit_drug(request, drug_id):
    #登录验证
    if not request.session.get('is_logged_in'):
        return redirect('login')
    drug = get_object_or_404(Drug, pk=drug_id)  # 使用 pk 参数来获取主键
    if request.method == 'POST':
        # 从表单获取数据
        drug_name = request.POST.get('drug_name')
        drug_company = request.POST.get('drug_company')
        drug_quantity = request.POST.get('drug_quantity')
        drug_code = request.POST.get('drug_code')

        # 更新药品信息
        drug.drug_name = drug_name
        drug.drug_company = drug_company
        drug.drug_quantity = drug_quantity
        drug.drug_code = drug_code
        drug.save()

        # 向用户显示成功消息
        messages.success(request, '药品信息更新成功！')

        # 重定向到主页
        return redirect('home')
    else:
        # 如果不是 POST 请求，则显示编辑表单
        return render(request, 'accounts/edit_drug.html', {'drug': drug})
# 删除药品
@login_required
def delete_drug(request, drug_id):
    #登录验证
    if not request.session.get('is_logged_in'):
        return redirect('login')
    Drug.objects.get(id=drug_id).delete()
    messages.success(request, '药品删除成功！')
    return redirect('home')