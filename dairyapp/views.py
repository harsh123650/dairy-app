from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from .models import MilkDelivery, MilkingLog, HealthLog
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'dairyapp/index.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        # Hardcoded admin login
        if username == "Harshal123" and password == "Harshal@123":
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('admin_dashboard')

        # Regular user authentication
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.groups.filter(name='Admin').exists():
                return redirect('admin_dashboard')
            elif user.groups.filter(name='Staff').exists():
                return redirect('staff_dashboard')
            elif user.groups.filter(name='Worker').exists():
                return redirect('worker_dashboard')
            elif user.groups.filter(name='Customer').exists():
                return redirect('customer_dashboard')

        return render(request, 'dairyapp/login.html', {'error': 'Invalid credentials'})
    return render(request, 'dairyapp/login.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def admin_dashboard(request):
    context = {
        'latest_delivery': MilkDelivery.objects.last(),
        'milking_data': MilkingLog.objects.last(),
        'health_data': HealthLog.objects.last(),
        'all_deliveries': MilkDelivery.objects.all(),
        'all_milking': MilkingLog.objects.all(),
        'all_health': HealthLog.objects.all(),
        'all_users': User.objects.all()
    }
    return render(request, 'dairyapp/admin.html', context)

@login_required
def staff_dashboard(request):
    if request.method == 'POST':
        MilkDelivery.objects.create(
            customer_id=request.POST['customer_id'],
            date=request.POST['date'],
            time=request.POST['time']
        )
    return render(request, 'dairyapp/staff.html')

@login_required
def worker_dashboard(request):
    if request.method == 'POST':
        MilkingLog.objects.create(
            milk_time=request.POST['milk_time'],
            milk_quantity=request.POST['milk_quantity']
        )
        HealthLog.objects.create(
            health_notes=request.POST['health_notes']
        )
    return render(request, 'dairyapp/worker.html')

@login_required
def customer_dashboard(request):
    latest_delivery = MilkDelivery.objects.last()
    health_logs = HealthLog.objects.all()
    return render(request, 'dairyapp/customer.html', {
        'latest_delivery': latest_delivery,
        'health_logs': health_logs
    })

@login_required
def create_user_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        group_name = request.POST['group']
        user = User.objects.create_user(username=username, password=password)
        group, created = Group.objects.get_or_create(name=group_name)
        user.groups.add(group)
        return redirect('admin_dashboard')
    return redirect('admin_dashboard')
