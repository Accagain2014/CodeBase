#coding=utf-8
import time, datetime
import dateutil.relativedelta

'''
Judge whether a year is a leap year or not
'''
def is_leap(year):
	if ((year % 4 == 0) and (year % 100)) or (year % 400 == 0):
		return 1
	return 0

'''
Get num of days the date have
'''
def month_days(date, date_format='%Y-%m-%d'):
	days = [
	[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
	[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

	date = datetime.datetime.strptime(date, date_format)
	leap = is_leap(date.year)
	return days[leap][date.month-1]

'''
Get date range by day
'''
def get_range_days(start_str, days=1, date_format='%Y-%m-%d'):
	"""
	args: 	start_str, 开始日期字符串
			dyas,	一共多少天(包含开始日期)
			date_format,	日期格式
	return:	返回日期字符串数组
	"""
	### %Y %m %d %H %M %S
	start_date = datetime.datetime.strptime(start_str, date_format)

	return [(start_date + datetime.timedelta(days=_)).strftime(date_format) \
		for _ in range(days)]
	

def get_range(start_str, end_str, date_format='%Y-%m-%d'):
	"""
	args:	start_str, 开始日期字符串
			end_str, 结束日期字符串
			date_format, 日期格式
	return:	返回日期字符串数组
	"""
	start_date = datetime.datetime.strptime(start_str, date_format)
	end_date = datetime.datetime.strptime(end_str, date_format)
	days = (end_date - start_date).days
	return get_range_days(start_str, days)


def move_days(start_str, days=1, date_format='%Y-%m-%d'):
	"""
	args:	start_str, 开始日期字符串
			days,	移动天数
	return:	返回往后推迟天数后是第几天
	"""
	start_date = datetime.datetime.strptime(start_str, date_format)
	return (start_date + datetime.timedelta(days=days)).strftime(date_format)


def get_diff_days(start_str, end_str, date_format='%Y-%m-%d'):
	"""
	args:	start_str, 开始日期字符串
			end_str, 结束日期字符串
	return:	返回中间间隔的天数
	examples:
			get_diff_days('2016-02-01', '2016-02-03')
			return 2
	"""
	start_date = datetime.datetime.strptime(start_str, date_format)
	end_date = datetime.datetime.strptime(end_str, date_format)
	days = (end_date - start_date).days
	return days

def get_pre_month(date='2016-05-28', months=1, date_format='%Y-%m-%d'):
	date = datetime.datetime.strptime(date, date_format)
	date += dateutil.relativedelta.relativedelta(months=-months)
	#print help(date)
	#date = datetime.datetime_offset_by_month(date, 1)
	return date.strftime(date_format)



if __name__ == '__main__':
	print get_pre_month('2016-01-28', 0)
	print move_days('2016-02-01', month_days('2016-02-01'))
	print month_days('2016-11-30')
	print get_range('2016-05-28', '2016-06-01')
	print move_days('2016-02-27', 2)
	print get_range_days('2016-02-27', 5)
	print get_diff_days('2016-02-01', '2016-02-03')
	print get_pre_month('2016-01-28')
	#print help(datetime.timedelta)
	#print help(datetime)
