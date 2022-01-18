from flask import Flask, render_template, request, redirect, url_for
from Forms import CreateSupplierForm, CreateOrderForm
import shelve, Inventory

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
            supplier_list = []
            for key in suppliers_dict:
                suppliers = suppliers_dict.get(key)
                supplier_list.append(suppliers)
            for key in supplier_list:
                Inventory.Supplier.count_id = key.get_id()
        except:
            print('Error in retrieving db')
        supplier = Inventory.Supplier(create_supplier_form.supplier_name.data,
                                      create_supplier_form.name.data,
                                      create_supplier_form.phone.data,
                                      create_supplier_form.address.data,
                                      create_supplier_form.email.data,create_supplier_form.email.data,)
        suppliers_dict[supplier.get_id()] = supplier
        db['Suppliers'] = suppliers_dict

        # Test codes
        suppliers_dict = db['Suppliers']
        supplier = suppliers_dict[supplier.get_id()]
        print(supplier.get_supplier_name(), supplier.get_name(),
              "was stored in supplier.db successfully with supplier_id ==",
              supplier.get_id())

        db.close()

        return redirect(url_for('retrieve_suppliers'))
    return render_template('createSupplier.html', form=create_supplier_form)


@app.route('/createOrder', methods=['GET', 'POST'])
def create_order():
    create_order_form = CreateOrderForm(request.form)
    if request.method == 'POST':
        orders_dict = {}
        db = shelve.open('order.db', 'c')

        try:
            orders_dict = db['Orders']
            orders_list = []
            for key in orders_dict:
                orders = orders_dict.get(key)
                orders_list.append(orders)
            for key in orders_list:
                Inventory.Order.count_id = key.get_order_id()
        except:
            print("Error in retrieving Orders from order.db.")

        order = Inventory.Order(create_order_form.date.data,
                                create_order_form.purchase_order.data,
                                create_order_form.supplier.data,
                                create_order_form.delivery_date.data,
                                create_order_form.amount.data)
        orders_dict[order.get_id()] = order
        db['Orders'] = orders_dict

        # Test codes
        orders_dict = db['Orders']
        order = orders_dict[order.get_id()]
        print(order.get_date(), order.get_supplier(),
              "was stored in order.db successfully with order_id ==",
              order.get_id())

        db.close()

        return redirect(url_for('retrieve_orders'))
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

@app.route("/status_order/<int:id>/", methods=['POST'])
def status_order(id):
    db = shelve.open('order.db', 'w')
    orders_dict: dict = db['Orders']
    orders_id = orders_dict.get(id)
    if orders_id.get_order_status()=='Active': #if obj status is active
        print(f"Event Key {orders_id.get_id()} has been inactivated!")
        orders_id.set_order_status('Inactive') # it will then auto set to inactive
    else:
        print(f"Event Key {orders_id.get_id()} has been activated!")
        orders_id.set_order_status('Active')
    db['Orders'] = orders_dict
    db.close()
    return redirect(url_for("retrieve_orders"))


@app.route('/updateSupplier/<int:id>/', methods=['GET', 'POST'])
def update_supplier(id):
    update_supplier_form = CreateSupplierForm(request.form)
    if request.method == 'POST' and update_supplier_form.validate():
        suppliers_dict = {}
        db = shelve.open('supplier.db', 'w')
        suppliers_dict = db['Suppliers']

        supplier = suppliers_dict.get(id)
        supplier.set_supplier_name(update_supplier_form.supplier_name.data)
        supplier.set_name(update_supplier_form.name.data)
        supplier.set_phone(update_supplier_form.phone.data)
        supplier.set_address(update_supplier_form.address.data)
        supplier.set_email(update_supplier_form.email.data)
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
        update_supplier_form.supplier_name.data = supplier.get_supplier_name()
        update_supplier_form.name.data = supplier.get_name()
        update_supplier_form.phone.data = supplier.get_phone()
        update_supplier_form.address.data = supplier.get_address()
        update_supplier_form.email.data = supplier.get_email()
        update_supplier_form.remarks.data = supplier.get_remarks()

        return render_template('updateSupplier.html', form=update_supplier_form)


@app.route('/updateOrder/<int:id>/', methods=['GET', 'POST'])
def update_order(id):
    update_order_form = CreateOrderForm(request.form)
    if request.method == 'POST':
        orders_dict = {}
        db = shelve.open('order.db', 'w')
        orders_dict = db['Orders']

        order = orders_dict.get(id)
        order.set_date(update_order_form.date.data)
        order.set_purchase_order(update_order_form.purchase_order.data)
        order.set_supplier(update_order_form.supplier.data)
        order.set_delivery_date(update_order_form.delivery_date.data)
        order.set_order_status(update_order_form.order_status.data)
        order.set_amount(   update_order_form.amount.data)

        db['Orders'] = orders_dict
        db.close()

        return redirect(url_for('retrieve_orders'))
    else:
        orders_dict = {}
        db = shelve.open('order.db', 'r')
        orders_dict = db['Orders']
        db.close()

        order = orders_dict.get(id)
        update_order_form.date.data = order.get_date()
        update_order_form.purchase_order.data = order.get_purchase_order()
        update_order_form.supplier.data = order.get_supplier()
        update_order_form.delivery_date.data = order.get_delivery_date()
        update_order_form.order_status.data = order.get_order_status()
        update_order_form.amount.data = order.get_amount()

        return render_template('updateOrder.html', form=update_order_form)

@app.route('/deleteSupplier/<int:id>', methods=['POST'])
def delete_supplier(id):
    suppliers_dict = {}
    db = shelve.open('supplier.db', 'w')
    suppliers_dict = db['Suppliers']

    suppliers_dict.pop(id)

    db['Suppliers'] = suppliers_dict
    db.close()

    return redirect(url_for('retrieve_suppliers'))

@app.route('/deleteOrder/<int:id>', methods=['POST'])
def delete_order(id):
    orders_dict = {}
    db = shelve.open('order.db', 'w')
    orders_dict = db['Orders']

    orders_dict.pop(id)

    db['Orders'] = orders_dict
    db.close()

    return redirect(url_for('retrieve_orders'))


if __name__ == '__main__':
    app.run(debug=True)
