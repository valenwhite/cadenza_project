from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email


#Checkout Form
class CheckoutForm(FlaskForm):
    firstname = StringField("First Name", validators=[InputRequired()])
    lastname = StringField("Last Name", validators=[InputRequired()])
    email = StringField("Your Email")
    phone = StringField("Your Phone Number", validators=[InputRequired()])
    address = StringField("Your address", validators=[InputRequired()])
    city = StringField("Your city", validators=[InputRequired()])
    state = StringField("Your state", validators=[InputRequired()])
    post_code = StringField("Your postcode", validators=[InputRequired()])
    submit = SubmitField("Send to agent")