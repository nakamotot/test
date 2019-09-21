import ui
import csv
import re
 
v = ui.load_view('test')

data = []
listname = []
def setData():
	
	def showData(sender):
		_index = ds.selected_row
		
		v['debug'].text = 'price:'+str(data[_index]['price'])
		_data = ui.ListDataSource(['price:'+str(data[_index]['price']),'quantity:'+str(data[_index]['quantity']),'totalprice:'+str(data[_index]['totalprice'])])
		dataTable.data_source = dataTable.delegate = _data
		dataTable.reload_data()
	
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
		
		setData()	
		v['debug'].text = _totalprice
		
	def deleteRow(sender):
		_index = ds.selected_row
		lines = list()
		
		f = open('test.csv')
		reader = csv.reader(f)
		
		for row in reader:
			lines.append(row)
			
		lines.pop(_index)	
		
		print(lines)
					
		v['debug'].text = str(ds.items[_index])
#----------------------- funcitons ^ -----------------



	data = []
	listname = []
	
	f=open('test.csv')
	reader = csv.DictReader(f)
	l=[row for row in reader]
	
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
		
		deleteBtn = v['scrollview1']['delete']
		deleteBtn.action = deleteRow
		
		f.close()

setData()

v.present('sheet')

