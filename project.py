import mysql.connector as con
import time

db = con.connect(
	host="localhost",
	user="root",
	passwd="clgws123", 
	database="clgws")

cur = db.cursor()

def show_all(table_name):
	com = f"SELECT * FROM {table_name}"
	cur.execute(com)
	return cur.fetchall()

def new_id(table_name, column_name):
	com = f"SELECT MAX({column_name}) FROM {table_name}"
	cur.execute(com)
	previous_id = cur.fetchone()[0]
	if previous_id is None:
		return 1
	return previous_id + 1

def add_new_record(table_name, column_names, column_values):
	com = f"""INSERT INTO {table_name}({column_names}) 
	VALUES({column_values})"""
	cur.execute(com)
	db.commit()
	return

def update_record(table_name, id_name, id_value, column_name, column_value):
	com = f"""UPDATE {table_name} 
	SET {column_name} = {column_value} WHERE {id_name} = {id_value}"""
	cur.execute(com)
	db.commit()
	return

while True:
	option = input("""
Enter your option 0-12:
(0) Exit
(1) Show all existing car listings in inventory
(2) Add new car listing
(3) Modify quantity in existing car listing
(4) Show all existing customers
(5) Add new customer in database
(6) Modify details of existing customer in database
(7) Show all active orders
(8) Add new active order
(9) Mark existing active order as complete
(10) Show all completed orders
""")

	# Option 0 = Exit
	if option == "0":
		print("Thank you. Exiting the program now.")
		break

	# option 1 = Show all existing car listings in inventory 
	elif option == "1":
		for listing in show_all("Inventory"):
			print(listing)
		time.sleep(2.5)

	# option 2 = Add new car listing
	elif option == "2":
		car_id = new_id("Inventory", "Car_ID")
		make = input("Enter Make of new car listing: ")
		model = input("Enter Model of new car listing: ")
		colour = input("Enter Colour of new car listing: ")

		try:
			quantity  = int(input("Enter quantity of new car listing: "))
		except:
			print("The quantity entered is invalid.")
			print("Listing not added. Please try again.")
			continue

		column_names = "Car_ID, Make, Model, Colour, Quantity"
		column_values = f"""{car_id}, "{make}", "{model}", "{colour}", {quantity}"""
		add_new_record("Inventory", column_names, column_values)

		print("Listing added.")

	# option 3 = Modify quantity in existing car listing
	elif option == "3":
		try:
			car_id = int(input("Enter Car ID to update: "))
			quantity  = int(input("Enter updated quantity: "))
		except:
			print("The quantity or Car ID entered is invalid.")
			print("Listing not updated. Please try again.")
			continue

		update_record("Inventory", "Car_ID", car_id, "Quantity", quantity)
		print("Record updated.")

	# option 4 = Show all existing customers
	elif option == "4":
		for customer in show_all("Customer"):
			print(customer)
		time.sleep(2.5)

	# option 5 = Add new customer in database
	elif option == "5":
		cust_id = new_id("Customer", "Cust_ID")
		name = input("Enter Name of new customer: ")
		email = input("Enter Email of new customer: ")

		try:
			phone = int(input("Enter phone number of new customer: "))
		except:
			print("The phone number entered is invalid.")
			print("Customer not added. Please try again.")
			continue

		column_names = "Cust_ID, Name, Phone, Email"
		column_values = f"""{cust_id}, "{name}", {phone}, "{email}" """
		add_new_record("Customer", column_names, column_values)

		print("Customer added.")

	# option 6 = Modify details of existing customer in database
	elif option == "6":
		try:
			cust_id = int(input("Enter Customer ID to update: "))
		except:
			print("The Customer ID entered is invalid.")
			print("Customer not updated. Please try again.")
			continue

		column_name = input("Enter column to update: ").title()
		
		if column_name == "Email":
			column_value = input("Enter updated Email: ")
		
		elif column_name == "Phone":
			try:
				column_value = int(input("Enter updated Phone number: "))
			except:
				print("The Phone number entered is invalid.")
				print("Customer not updated. Please try again.")
				continue

		else:
			print("The Column name entered is invalid.")
			print("Customer not updated. Please try again.")
			continue

		update_record("Customer", "Cust_ID", cust_id, column_name, column_value)
		print("Record updated.")

	# option 7 = Show all active orders
	elif option == "7":
		for order in show_all("Active_orders"):
			print(order)
		time.sleep(2.5)

	# option 8 = Add new active order
	elif option == "8": 
		order_id = new_id("Active_orders", "Order_ID")
		date_of_order = time.strftime("%Y-%m-%d")
		car_id = input("Enter Car ID of order: ")
		cust_id = input("Enter Customer ID of order: ")

		try:
			column_names = "Order_ID, Date_of_order, Car_ID, Cust_ID"
			column_values = f"""{order_id}, "{date_of_order}", {car_id}, {cust_id}"""
			add_new_record("Active_orders", column_names, column_values)
		except:
			print("The Customer ID or Car ID entered is invalid.")
			print("Order not added. Please try again.")
			continue

		print("Order added.")

	# option 9 = Mark existing active order as complete
	elif option == "9": 
		try:
			order_id = int(input("Enter order ID to mark as complete: "))
		except:
			print("The Order ID entered is invalid.")
			print("Order not marked as complete. Please try again.")
			continue

		try:
			cur.execute(f"SELECT * from Active_orders WHERE Order_ID = {order_id}")
			date_of_order, car_id, cust_id = cur.fetchone()[1:]
		except:
			print("The Order ID entered is invalid.")
			print("Order not marked as complete. Please try again.")
			continue

		cur.execute(f"DELETE FROM Active_Orders WHERE Order_ID = {order_id}")

		order_id = new_id("Completed_orders", "Order_ID")
		date_completed = time.strftime("%Y-%m-%d")
		column_names = "Order_ID, Date_of_order, Car_ID, Cust_ID, Date_completed"
		column_values = f"""{order_id}, "{date_of_order}", {car_id}, {cust_id}, "{date_completed}" """

		add_new_record("Completed_orders", column_names, column_values)
		print("Record updated.")

	# option 10 = Show all completed orders
	elif option == "10":
		for order in show_all("Completed_orders"):
			print(order)
		time.sleep(2.5)

	# catch all menu option
	else:
		print("Invalid menu option. Please try again.")










