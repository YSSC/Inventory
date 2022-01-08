from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateSupplierForm, CreateOrderForm
import shelve, Supplier, Order


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/createSupplier', methods=['GET', 'POST'])
def create_supplier():
    create_supplier_form = CreateSupplierForm(request.form)
    if request.method == 'POST' and create_supplier_form.validate():
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'c')

        try:
            suppliers_dict = db['Suppliers']
        except:
            print("Error in retrieving Suppliers from supplier.db.")

        supplier = Supplier.Supplier(create_supplier_form.first_name.data, create_supplier_form.last_name.data, create_supplier_form.gender.data, create_supplier_form.membership.data, create_supplier_form.remarks.data)
        suppliers_dict[supplier.get_supplier_id()] = supplier
        db['Suppliers'] = suppliers_dict

        # Test codes
        suppliers_dict = db['Suppliers']
        supplier = suppliers_dict[supplier.get_supplier_id()]
        print(supplier.get_first_name(), supplier.get_last_name(), "was stored in supplier.db successfully with supplier_id ==", supplier.get_supplier_id())

        db.close()

        return redirect(url_for('retrieve_suppliers'))
    return render_template('createSupplier.html', form=create_supplier_form)

@app.route('/createOrder', methods=['GET', 'POST'])
def create_order():
    create_order_form = CreateOrderForm(request.form)
    if request.method == 'POST' and create_order_form.validate():
        orders_dict = {}
        db = shelve.open('order.db', 'c')

        try:
            orders_dict = db['Orders']
        except:
            print("Error in retrieving Orders from order.db.")

        order = Order.Order(create_order_form.first_name.data, create_order_form.last_name.data,
                                     create_order_form.gender.data, create_order_form.membership.data,
                                     create_order_form.remarks.data, create_order_form.email.data,
                                     create_order_form.date_joined.data,
                                     create_order_form.address.data, )
        orders_dict[order.get_order_id()] = order
        db['Orders'] = orders_dict

        db.close()

        return redirect(url_for('home'))
    return render_template('createOrder.html', form=create_order_form)

@app.route('/retrieveSuppliers')
def retrieve_suppliers():
    suppliers_dict = {}
    db = shelve.open('supplier.db', 'r')
    suppliers_dict = db['Suppliers']
    db.close()

    suppliers_list = []
    for key in suppliers_dict:
        supplier = suppliers_dict.get(key)
        suppliers_list.append(supplier)

    return render_template('retrieveSuppliers.html', count=len(suppliers_list), suppliers_list=suppliers_list)

@app.route('/retrieveOrders')
def retrieve_orders():
    orders_dict = {}
    db = shelve.open('order.db', 'r')
    orders_dict = db['Orders']
    db.close()

    orders_list = []
    for key in orders_dict:
        order = orders_dict.get(key)
        orders_list.append(order)

    return render_template('retrieveOrders.html', count=len(orders_list), orders_list=orders_list)

@app.route('/updateSupplier/<int:id>/', methods=['GET', 'POST'])
def update_supplier(id):
    update_supplier_form = CreateSupplierForm(request.form)
    if request.method == 'POST' and update_supplier_form.validate():
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'w')
        suppliers_dict = db['Suppliers']

        supplier = suppliers_dict.get(id)
        supplier.set_first_name(update_supplier_form.first_name.data)
        supplier.set_last_name(update_supplier_form.last_name.data)
        supplier.set_gender(update_supplier_form.gender.data)
        supplier.set_membership(update_supplier_form.membership.data)
        supplier.set_remarks(update_supplier_form.remarks.data)

        db['Suppliers'] = suppliers_dict
        db.close()

        return redirect(url_for('retrieve_suppliers'))
    else:
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'r')
        suppliers_dict = db['Suppliers']
        db.close()

        supplier = suppliers_dict.get(id)
        update_supplier_form.first_name.data = supplier.get_first_name()
        update_supplier_form.last_name.data = supplier.get_last_name()
        update_supplier_form.gender.data = supplier.get_gender()
        update_supplier_form.membership.data = supplier.get_membership()
        update_supplier_form.remarks.data = supplier.get_remarks()

        return render_template('updateSupplier.html', form=update_supplier_form)

@app.route('/updateOrder/<int:id>/', methods=['GET', 'POST'])
def update_order(id):
    update_order_form = CreateOrderForm(request.form)
    if request.method == 'POST' and update_order_form.validate():
        orders_dict = {}
        db = shelve.open('order.db', 'w')
        orders_dict = db['Orders']

        order = orders_dict.get(id)
        order.set_first_name(update_order_form.first_name.data)
        order.set_last_name(update_order_form.last_name.data)
        order.set_gender(update_order_form.gender.data)
        order.set_membership(update_order_form.membership.data)
        order.set_remarks(update_order_form.remarks.data)

        db['Orders'] = orders_dict
        db.close()

        return redirect(url_for('retrieve_orders'))
    else:
        orders_dict = {}
        db = shelve.open('order.db', 'r')
        orders_dict = db['Orders']
        db.close()

        order = orders_dict.get(id)
        update_order_form.first_name.data = order.get_first_name()
        update_order_form.last_name.data = order.get_last_name()
        update_order_form.gender.data = order.get_gender()
        update_order_form.membership.data = order.get_membership()
        update_order_form.remarks.data = order.get_remarks()

        return render_template('updateOrder.html', form=update_order_form)


if __name__ == '__main__':
    app.run()
