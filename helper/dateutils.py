#coding=utf-8
import time, datetime
import dateutil.relativedelta

'''
	Common date operation functions.
'''


def is_leap(year):
	'''
	Judge whether a year is a leap year or not
	'''
	if ((year % 4 == 0) and (year % 100)) or (year % 400 == 0):
		return 1
	return 0


def month_days(date, date_format='%Y-%m-%d'):
	'''
	Get num of days the date have
	'''
	days = [
	[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
	[31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]]

	date = datetime.datetime.strptime(date, date_format)
	leap = is_leap(date.year)
	return days[leap][date.month-1]


def get_range_days(start_str, days=1, date_format='%Y-%m-%d'):
	'''
	Get date range by day

	args: 	start_str, 开始日期字符串
			dyas,	一共多少天(包含开始日期)
			date_format,	日期格式
	return:	返回日期字符串数组
	'''
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


def produce_value_day_range(values, day_range, value_name='value', day_name='day'):
	'''
		args:
			values: list 
			date_range: list
		return:
			for every value in values, produce every day in day_range to attach
		examples:
			produce_value_day_range(['1', '2', '3'], ['2015-01-01', '2015-01-02', '2015-01-03'])
			
			return :
				value_name,day_name
				1,2015-01-01
				1,2015-01-02
				1,2015-01-03
				2,2015-01-01
				2,2015-01-02
				2,2015-01-03
				3,2015-01-01
				3,2015-01-02
				3,2015-01-03
	'''
	values_range_frame = pd.DataFrame({value_name: values, 'tmp': 1})
	day_range_frame = pd.DataFrame({day_name: day_range, 'tmp': 1})
	values_day_frame = pd.merge(values_range_frame, day_range_frame, on='tmp', how='left')
	values_day_frame = values_day_frame.drop('tmp', axis=1)
	return values_day_frame


def get_feature_value_map(frame, feature):
	'''
		用于对一些中文字符串进行映射
	'''
	frame[feature] = frame[feature].map(lambda x: (str(x)).strip())
	values = list(frame[feature].drop_duplicates())
	ans = {}
	for one in values:
		ans[one] = values.index(one) + 1
	return ans


def readFromTable(fileName, names=None):
	return pd.read_table(fileName, sep=' ', index_col=False, header=None, names=names)


if __name__ == '__main__':
	help(is_leap)
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
