from django.urls import path
from .views import WaterFlowList, WaterFlowDetail, DailyAverageFlow, WeeklyAverageFlow, MonthlyTotalFlow

app_name = 'flowrate'

urlpatterns = [
    path('flowrate/list/', WaterFlowList, name='flowrate_list'),
    path('flowrate/detail/<str:serial_number>/', WaterFlowDetail, name='flowrate_detail'),
    path('flowrate/average/daily/<str:serial_number>/', DailyAverageFlow, name='daily_average_flow'),
    path('flowrate/average/weekly/<str:serial_number>/', WeeklyAverageFlow, name='weekly_average_flow'),
    path('flowrate/total/monthly/<str:serial_number>/', MonthlyTotalFlow, name='monthly_total_flow'),
]