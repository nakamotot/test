import ui
import console
import csv

def clicked(sender):
	#f=open('test.csv','w+')
	#f.write('test')
	#f.close()
	v['debug'].text = 'test debug'

def showData(sender):
	#print(ds.selected_row + 1)
	_index = ds.selected_row
	v['debug'].text = 'price:'+str(data[_index]['price'])

f=open('test.csv')
reader = csv.DictReader(f)
l=[row for row in reader]


data = []
listname = []
for index,item in enumerate(l):
	_data={'id':index,'name':item['name'],'price':item['price'],'quantity':item['quantity']}
	data.append(_data)
	listname.append(_data['name'])			

v = ui.load_view('test')
table = v['table1']
ds = ui.ListDataSource(listname)
#ds.action = showData
table.data_source = table.delegate = ds
#table.data_source = ds
table.reload_data()
ds.action = showData
table.allows_selection = True
button = v['button1']
button.title = 'data'
v.present('sheet')
