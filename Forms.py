from wtforms import Form, StringField, RadioField, SelectField, TextAreaField, validators
from wtforms import EmailField, DateField

class CreateSupplierForm(Form):
    supplier_name = StringField('Supplier Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    name = StringField('Name', [validators.Length(min=1, max=150), validators.DataRequired()])
    phone = StringField('Phone', [validators.Length(min=1, max=150), validators.DataRequired()])
    address = TextAreaField('Mailing Address', [validators.length(max=200), validators.DataRequired()])
    email = EmailField('Email', [validators.Email(), validators.DataRequired()])
    remarks = TextAreaField('Remarks', [validators.Optional()])

class CreateOrderForm(Form):
    date = DateField('Date', format='%Y-%m-%d')
    purchase_order = StringField('Purchase Order', [validators.Length(min=1, max=150), validators.DataRequired()])
    supplier = StringField('Supplier', [validators.Length(min=1, max=150), validators.DataRequired()])
    delivery_date = DateField('Date', format='%Y-%m-%d')
    order_status = StringField('Order Status', [validators.Length(min=1, max=150), validators.DataRequired()])
    amount = StringField('Amount', [validators.Length(min=1, max=150), validators.DataRequired()])

