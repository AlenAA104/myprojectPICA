from django.shortcuts import render,HttpResponse,redirect
from .models import Record,Category
from .forms import RecordForm
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required #使用者必須通過
def hello(request):
    return HttpResponse('hello world')
@login_required #使用者必須通過
def index(request):
    user = request.user
    record_form =RecordForm(user=user,initial={'balance_type':'支出'})#initial給初始直
    records = Record.objects.filter(user = user)
    income_list = [record.cash for record in records if record.balance_type=='收入']
    outcome_list =[record.cash for record in records if record.balance_type =='支出']
    income = sum(income_list) if len(income_list)!=0 else 0
    outcome = sum(outcome_list) if len(outcome_list)!=0 else 0
    net=income-outcome
    return render(request,'app/Index.html',locals())
@login_required #使用者必須通過
def index1(request):
    return render(request,'app/index1.html',{'key':'a'})
@login_required #使用者必須通過
def settings(request):
    user = request.user
    categories = Category.objects.filter(user = user)
    return render(request,'app/settings.html',locals())
@login_required #使用者必須通過
def add_category(request):
    if request.method == 'POST':
        user = request.user
        posted_data = request.POST#存取用post屬性傳進來的資料
        category=posted_data['add_category']#透過NAME取值
        Category.objects.get_or_create(category=category,user = user)#新增
        return redirect('/settings')#可以幫你自動導到

@login_required  # 使用者必須通過
def deleteCategory(request,category):
    user = request.user
    Category.objects.filter(category=category,user = user).delete()
    return redirect('/settings')  # 可以幫你自動導到
@login_required #使用者必須通過
def add_Record(request):
    if request.method =='POST':
        user = request.user
        form = RecordForm(user,request.POST)#相當於把FORM的值
        if form.is_valid():#驗證?
            record = form.save(commit=False)
            record.user = user
            form.save()#值存入MODEL
    return redirect('/index')
@login_required #使用者必須通過
def deleteRecord(request):
    if request.method =='POST':
        id=request.POST['delete_val']
        Record.objects.filter(id=id).delete()
    return redirect('/index')
