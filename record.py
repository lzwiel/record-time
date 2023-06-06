import datetime

# 输入年月日，返回datetime对象
def get_date(year, month, day):
    return datetime.datetime(year, month, day)

# 记录每天早上是否按时起床
def record_wake_up_on_time(date, on_time):
    with open('wake_up_records.txt', 'a') as f:
        f.write(f'{date} {on_time}\n')

# 记录每天晚上是否按时睡觉
def record_go_to_bed_on_time(date, on_time):
    with open('go_to_bed_records.txt', 'a') as f:
        f.write(f'{date} {on_time}\n')

# 获取当前日期
now = datetime.datetime.now()
today = get_date(now.year, now.month, now.day)

# 记录今天是否按时起床
print('Did you wake up on time today?')
wake_up = input().lower()
if wake_up in ['yes', 'y']:
    record_wake_up_on_time(today, True)
else:
    record_wake_up_on_time(today, False)

# 记录今天是否按时睡觉
print('Did you go to bed on time last night?')
go_to_bed = input().lower()
if go_to_bed in ['yes', 'y']:
    record_go_to_bed_on_time(today, True)
else:
    record_go_to_bed_on_time(today, False)
    
#这个程序会要求你输入当天早上和晚上是否按时起床或睡觉，并将记录写入名为 "wake_up_records.txt" 和 "go_to_bed_records.txt" 的两个文件中。你可以每天运行这个程序来记录你的习惯，以便以后分析和改进。
