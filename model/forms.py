from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

class DataEntryForm(FlaskForm):
    
    Status = SelectField(label='Status', choices=['Unknown','Under Construction', 'Ready to Move'], validators=[DataRequired()])
    Furnished_status = SelectField(label='Furnished status', choices=['Unknown', 'Furnished', 'Unfurnished', 'Semi-Furnished'], validators=[DataRequired()])
    neworold = SelectField(label='New or Old', choices=['Unknown', 'New Property', 'Resale'], validators=[DataRequired()])
    type_of_building = SelectField(label='Type of Building', choices=['Unknown', 'Flat', 'Individual House'], validators=[DataRequired()])
    area = StringField(label='Area (sqft)', validators=[DataRequired()])
    lattitude = StringField(label='Lattitude', validators=[DataRequired()])
    longitude = StringField(label='Longitude', validators=[DataRequired()])
    Bedrooms = StringField(label='Bedrooms', validators=[DataRequired()])
    Bathrooms = StringField(label='Bathrooms', validators=[DataRequired()])
    Balcony = StringField(label='Balcony', validators=[DataRequired()])
    parking = StringField(label='Parking', validators=[DataRequired()])
    Lift = StringField(label='Lift', validators=[DataRequired()])
    submit = SubmitField(label='Check Price')