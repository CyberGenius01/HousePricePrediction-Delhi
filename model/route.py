from flask import redirect, render_template, request, url_for, redirect
from model import app
from model.prediction import predictResult
from model.forms import DataEntryForm
import numpy as np

@app.route('/', methods = ['GET', 'POST'])
def home_page():
    form = DataEntryForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            area = form.area.data
            lattitude = form.lattitude.data
            longitude = form.longitude.data
            Bedrooms = form.Bedrooms.data
            Bathrooms = form.Bathrooms.data
            Balcony = form.Balcony.data
            parking = form.parking.data
            Lift = form.Lift.data
            Status = form.Status.data
            Furnished_status = form.Furnished_status.data
            neworold = form.neworold.data
            type_of_building = form.type_of_building.data
            print([Status,Furnished_status,neworold,type_of_building,
            area,lattitude,longitude,Bedrooms,Bathrooms,Balcony,
            parking,Lift])
            return redirect(url_for('predict_page', area=area, lattitude=lattitude,
                                    longitude=longitude, Bedrooms=Bedrooms,
                                    Bathrooms=Bathrooms, Balcony=Balcony,
                                    parking=parking, Lift=Lift, Status=Status,
                                    Furnished_status=Furnished_status,
                                    neworold=neworold, type_of_building=type_of_building))
        
    return render_template('home.html', form=form)

    print(np.array(request.args.get('test_data')).reshape(1,6))
    
@app.route('/price')
def predict_page():
    area = int(request.args.get('area'))
    lattitude = float(request.args.get('lattitude'))
    longitude = float(request.args.get('longitude'))
    Bedrooms = int(request.args.get('Bedrooms'))
    Bathrooms = int(request.args.get('Bathrooms'))
    Balcony = int(request.args.get('Balcony'))
    parking = int(request.args.get('parking'))
    Lift = int(request.args.get('Lift'))
    Status = str(request.args.get('Status'))
    Furnished_status = str(request.args.get('Furnished_status'))
    neworold = str(request.args.get('neworold'))
    type_of_building = str(request.args.get('type_of_building'))

    data = [Status,Furnished_status,neworold,type_of_building,
            area,lattitude,longitude,Bedrooms,Bathrooms,Balcony,
            parking,Lift]
    result = predictResult(data)
    return render_template('prediction.html', result=result)