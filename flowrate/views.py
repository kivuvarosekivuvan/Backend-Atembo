from django.shortcuts import render
from django.shortcuts import render
from .models import FlowRate
from django.shortcuts import render,redirect
from datetime import timedelta, date
from django.db.models import Avg, Sum



def WaterFlowList(request):
    waterflow = FlowRate.objects.all()
    return render(request, "waterflow_list.html", {"waterflow": waterflow})



def WaterFlowDetail(request, serial_number):
    device_flowrate = FlowRate.objects.get(serial_number=serial_number)
    return render(request, "waterflow_detail.html", {"device_flowrate": device_flowrate})



def DailyAverageFlow(request, serial_number):
    device_flow_rates = FlowRate.objects.filter(serial_number=serial_number)
    daily_average = device_flow_rates.aggregate(avg_flow_rate=Avg('flow_rate'))['avg_flow_rate']
    return render(request, "daily_average_flow.html", {"daily_average": daily_average})



def WeeklyAverageFlow(request, serial_number):
    today = date.today()
    start_date = today - timedelta(days=7)
    device_flow_rates = FlowRate.objects.filter(serial_number=serial_number, date__range=(start_date, today))
    weekly_average = device_flow_rates.aggregate(avg_flow_rate=Avg('flow_rate'))['avg_flow_rate']
    return render(request, "weekly_average_flow.html", {"weekly_average": weekly_average})



def MonthlyTotalFlow(request, serial_number):
    today = date.today()
    start_date = today.replace(day=1)
    device_flow_rates = FlowRate.objects.filter(serial_number=serial_number, date__range=(start_date, today))
    monthly_total = device_flow_rates.aggregate(total_flow_rate=Sum('flow_rate'))['total_flow_rate']
    return render(request, "monthly_total_flow.html", {"monthly_total": monthly_total})