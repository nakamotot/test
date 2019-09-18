import ui
import console
import csv

def debug(sender):
	v['debug'].text = 'test debug'
	
def showToggleAddForm(sender):
	if addform.y == 0:
		addform.y = -560
	else:
		addform.y = 0
 
def addToList(sender):
	showToggleAddForm(sender)

	_name = addform['name'].text;
	_quantity = addform['quantity'].text
	_price = addform['price'].text
	_totalprice = str(int(addform['quantity'].text) * int(addform['price'].text))
	
	f=open('test.csv','a')
	f.write('\n'+_name + ',' + _quantity + ',' + _price + ',' + _totalprice)
	f.close()
	
	v['debug'].text = _totalprice
	
def showData(sender):
	_index = ds.selected_row
	
	v['debug'].text = 'price:'+str(data[_index]['price'])
	_data = ui.ListDataSource(['price:'+str(data[_index]['price']),'quantity:'+str(data[_index]['quantity']),'totalprice:'+str(data[_index]['totalprice'])])
	dataTable.data_source = dataTable.delegate = _data
	dataTable.reload_data()

f=open('test.csv')
reader = csv.DictReader(f)
l=[row for row in reader]

data = []
listname = []
for index,item in enumerate(l):
	_data={
		'id':index,
		'name':item['name'],
		'price':item['price'],
		'quantity':item['quantity'],
		'totalprice':item['totalprice']
		}
	data.append(_data)
	listname.append(_data['name'])
		
v = ui.load_view('test')

table = v['table1']

ds = ui.ListDataSource(listname)
ds.action = showData

table.data_source = table.delegate = ds
table.reload_data()
table.allows_selection = True

addform = v['addform']
addform.y = -540
addformSubmit = addform['submit']
addformSubmit.action = addToList

dataTable = v['scrollview1']['table']

button = v['button1']
button.title = 'Add Data'
button.action = showToggleAddForm
v.present('sheet')

