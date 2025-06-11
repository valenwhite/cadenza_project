from . import db

orderdetails = db.Table('orderdetails', 
    db.Column('order_id', db.Integer,db.ForeignKey('orders.id'), nullable=False),
    db.Column('product_id',db.Integer,db.ForeignKey('products.id'),nullable=False),
    db.PrimaryKeyConstraint('order_id', 'product_id') )

class Product(db.Model):

    __tablename__='products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    sub_headline = db.Column(db.String(64), nullable=False, default='Coming Soon')
    category = db.Column(db.String(64), nullable=False)
    description = db.Column(db.String(500), nullable=False, default='Coming Soon')
    price = db.Column(db.Float, nullable=False)
    size = db.Column(db.Integer, nullable=False,  default=0)
    scent_id = db.Column(db.Integer, db.ForeignKey('scents.id'))
    image_url = db.Column(db.String(200), nullable=False,  default=0)
    scent=db.relationship('Scent', backref='scent',lazy=True)
    

    def __repr__(self):
        str = 'ID: {}, Name: {}, Category: {}, Description: {} Price: {}, Size: {}, Scent: {}, Img URL: {} \n'
        str = str.format(self.id, self.name, self.category, self.description, self.price, self.size, self.scent_id, self.image_url)
        return str
    
class Order(db.Model):

    __tablename__='orders'

    id = db.Column(db.Integer, primary_key=True)
    payment_status = db.Column(db.Boolean, default = False)
    date = db.Column(db.DateTime)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(128))
    phone = db.Column(db.String(32))
    address = db.Column(db.String(64))
    city = db.Column(db.String(64))
    state = db.Column(db.String(64))
    post_code = db.Column(db.String(64))
    products = db.relationship("Product", secondary=orderdetails, backref="orders")
    
    def __repr__(self):
        str = 'ID: {}, Date: {}, First Name: {}, Last Name: {}, Email" {}, Phone: {}, Address: {}\n'
        str = str.format(self.id, self.date, self.first_name, self.last_name, self.email, self.phone, self.address)
        return str


class Scent(db.Model):

    __tablename__='scents'

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(64),nullable = False)
    description = db.Column(db.String(500), nullable = False)
    scent_note1 = db.Column(db.String(20),nullable = False)
    scent_note2 = db.Column(db.String(20),nullable = False)
    scent_note3 = db.Column(db.String(20),nullable = False)

    def __repr__(self):
        str = 'ID: {}, Name: {}, Description: {} \n'
        str = str.format(self.id, self.name, self.description)
        return str
