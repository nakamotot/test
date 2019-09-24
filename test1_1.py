import ui
import sqlite3

dbname = 'test.db'
#c.execute("CREATE TABLE stocks(name text , quantity real , price real, totalprice real)")
	#c.execute('drop table stocks')
	#c.execute("INSERT INTo stocks VALUES('apple',5,100,500)")

def insertDB(data):
	print(data['name'])
	conn = sqlite3.connect(dbname)
	c= conn.cursor()
	_totalprice = str(data['quantity'] * data['price'])
	c.execute("INSERT INTO stocks VALUES('"+data['name']+"',"+str(data['quantity'])+","+str(data['price'])+","+_totalprice+")")
	
	#for row in c.execute('SELECT*FROM stocks'):
		#print(row)
	
	conn.commit()
	conn.close()

def getData(query):
	_data = []
	conn = sqlite3.connect(dbname)
	c= conn.cursor()
	
	
	c.execute('PRAGMA table_info("stocks")')
	
	col_name = []
	for colname in c.fetchall():
		col_name.append(colname[1])
	
	for i,row in enumerate(c.execute(query)):
		_obj = {}
		for n,r in enumerate(row):
			_obj[col_name[n]]=r
		_data.append(_obj)
	conn.commit()
	conn.close()
	return _data

v = ui.load_view('test')

data = []
listname = []
def setData():
	
	def showData(sender):
		_index = ds.selected_row
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
		insertDB({"name":_name,"quantity":int(_quantity),"price":int(_price)})
		setData()	
		v['debug'].text = _totalprice
		
	def deleteRow(sender):
		_index = ds.selected_row
		query = 'delete from stocks where name == "'+data[_index]['name']+'"'
		conn = sqlite3.connect(dbname)
		c= conn.cursor()
		c.execute(query)
		conn.commit()
		conn.close()
		
	
	def update(sender):
		_index = ds.selected_row
		v['debug'].text = str(ds.items[_index])
#----------------------- funcitons ^ -----------------



	data = []
	listname = []
	
	data = getData('SELECT * FROM stocks')
	
	for item in data:
		listname.append(item['name'])
		
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
		
setData()

v.present('sheet')

