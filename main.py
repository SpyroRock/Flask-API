from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class WeatherModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather_state_name = db.Column(db.String(1000), nullable=False)
    weather_state_abbr = db.Column(db.String(1000), nullable=False)
    wind_direction_compass = db.Column(db.String(1000), nullable=False)
    created = db.Column(db.String(1000), nullable=False)
    applicable_date = db.Column(db.String(1000), nullable=False)
    min_temp = db.Column(db.Float, nullable=False)
    max_temp = db.Column(db.Float, nullable=False)
    the_temp = db.Column(db.Float, nullable=False)
    wind_speed = db.Column(db.Float, nullable=False)
    wind_direction = db.Column(db.Float, nullable=False)
    air_pressure = db.Column(db.Float, nullable=False)
    humidity = db.Column(db.Integer, nullable=False)
    visibility = db.Column(db.Float, nullable=False)
    predictability = db.Column(db.Integer, nullable=False)

    def __init__(self, id, weather_state_name, weather_state_abbr, wind_direction_compass, created, application_date, min_temp, max_temp, the_temp, wind_speed, wind_direction, air_pressure, humidity, visibility, predictability) -> None:
        self.id = id
        self.weather_state_name = weather_state_name
        self.weather_state_abbr = weather_state_abbr
        self.wind_direction_compass = wind_direction_compass
        self.created = created
        self.applicable_date = application_date
        self.min_temp = min_temp
        self.max_temp = max_temp
        self.the_temp = the_temp
        self.wind_speed = wind_speed
        self.wind_direction = wind_direction
        self.air_pressure = air_pressure
        self.humidity = humidity
        self.visibility = visibility
        self.predictability = predictability
        

    def __repr__(self) -> str:
        return f"Weather(weather_state_name = {self.weather_state_name}, weather_state_abbr={self.weather_state_abbr}, wind_direction_compass = {self.wind_direction_compass}, created = {self.created}, applicable_date = {self.applicable_date}, min_temp = {self.min_temp}, max_temp = {self.max_temp}, the_temp = {self.the_temp}, wind_speed = {self.wind_speed}, wind_direction = {self.wind_direction}, air_pressure = {self.air_pressure}, humidity = {self.humidity}, visibility = {self.visibility}, predictability = {self.predictability})"
        

weather_conditions_args = reqparse.RequestParser()
# weather_conditions_args.add_argument("id", type=int, help="Country id is required", required=True)
weather_conditions_args.add_argument("weather_state_name", type=str, help="Weather state name is required", required=True)
weather_conditions_args.add_argument("weather_state_abbr", type=str, help="Weather state abbr is required", required=True)
weather_conditions_args.add_argument("wind_direction_compass", type=str, help="Wind direction compass is required", required=True)
weather_conditions_args.add_argument("created", type=str, help="Created is required", required=True)
weather_conditions_args.add_argument("applicable_date", type=str, help="Applicable date is required", required=True)
weather_conditions_args.add_argument("min_temp", type=float, help="Min temp is required", required=True)
weather_conditions_args.add_argument("max_temp", type=float, help="Max temp is required", required=True)
weather_conditions_args.add_argument("the_temp", type=float, help="The temp is required", required=True)
weather_conditions_args.add_argument("wind_speed", type=float, help="Wind speed is required", required=True)
weather_conditions_args.add_argument("wind_direction", type=float, help="Wind direction id is required", required=True)
weather_conditions_args.add_argument("air_pressure", type=float, help="Air pressure is required", required=True)
weather_conditions_args.add_argument("humidity", type=int, help="Humidity is required", required=True)
weather_conditions_args.add_argument("visibility", type=float, help="Visibility is required", required=True)
weather_conditions_args.add_argument("predictability", type=int, help="Predictability is required", required=True)


weather_update_args = reqparse.RequestParser()
# weather_update_args.add_argument("id", type=int, help="Country id is required", required=True)
weather_update_args.add_argument("weather_state_name", type=str, help="Weather state name is required", required=True)
weather_update_args.add_argument("weather_state_abbr", type=str, help="Weather state abbr is required", required=True)
weather_update_args.add_argument("wind_direction_compass", type=str, help="Wind direction compass is required", required=True)
weather_update_args.add_argument("created", type=str, help="Created is required", required=True)
weather_update_args.add_argument("applicable_date", type=str, help="Applicable date is required", required=True)
weather_update_args.add_argument("min_temp", type=float, help="Min temp is required", required=True)
weather_update_args.add_argument("max_temp", type=float, help="Max temp is required", required=True)
weather_update_args.add_argument("the_temp", type=float, help="The temp is required", required=True)
weather_update_args.add_argument("wind_speed", type=float, help="Wind speed is required", required=True)
weather_update_args.add_argument("wind_direction", type=float, help="Wind direction id is required", required=True)
weather_update_args.add_argument("air_pressure", type=float, help="Air pressure is required", required=True)
weather_update_args.add_argument("humidity", type=int, help="Humidity is required", required=True)
weather_update_args.add_argument("visibility", type=float, help="Visibility is required", required=True)
weather_update_args.add_argument("predictability", type=int, help="Predictability is required", required=True)

resource_fields = {
    'id': fields.Integer,
    'weather_state_name': fields.String,
    'weather_state_abbr': fields.String,
    'wind_direction_compass': fields.String,
    'created': fields.String,
    'applicable_date': fields.String,
    'min_temp': fields.Float,
    'max_temp': fields.Float,
    'the_temp': fields.Float,
    'wind_speed': fields.Float,
    'wind_direction': fields.Float,
    'air_pressure': fields.Float,
    'humidity': fields.Integer,
    'visibility': fields.Float,
    'predictability': fields.Integer
}

class Weather(Resource):
    @marshal_with(resource_fields)
    def get(self, country_id):
        result = WeatherModel.query.filter_by(id=country_id).first()
        if not result:
            abort(404, message="Could not find country with that id...")
        return result  

    @marshal_with(resource_fields)
    def put(self, country_id):
        args = weather_conditions_args.parse_args()
        result = WeatherModel.query.filter_by(id=country_id).first()
        if result:
            abort(409, message="Country id taken...")
        weather = WeatherModel(country_id, 
                               args['weather_state_name'], 
                               args['weather_state_abbr'],
                               args['wind_direction_compass'],
                               args['created'],
                               args['applicable_date'],
                               args['min_temp'],
                               args['max_temp'],
                               args['the_temp'],
                               args['wind_speed'],
                               args['wind_direction'],
                               args['air_pressure'],
                               args['humidity'],
                               args['visibility'],
                               args['predictability'])
        
        db.session.add(weather)
        db.session.commit()
        return weather, 201

    @marshal_with(resource_fields)
    def patch(self, country_id):
        args = weather_update_args.parse_args()
        result = WeatherModel.query.filter_by(id=country_id).first()
        if not result:
            abort(404, message="Country doesn't exist...")

        if args['weather_state_name']:
            result.weather_state_name = args['weather_state_name']
        if args['weather_state_abbr']:
            result.weather_state_abbr = args['weather_state_abbr']
        if args['wind_direction_compass']:
            result.wind_direction_compass = args['wind_direction_compass']
        if args['created']:
            result.created = args['created']
        if args['applicable_date']:
            result.applicable_date = args['applicable_date']
        if args['min_temp']:
            result.min_temp = args['min_temp']
        if args['max_temp']:
            result.max_temp = args['max_temp']
        if args['the_temp']:
            result.the_temp = args['the_temp']
        if args['wind_speed']:
            result.wind_speed = args['wind_speed']
        if args['wind_direction']:
            result.wind_direction = args['wind_direction']
        if args['air_pressure']:
            result.air_pressure = args['air_pressure']
        if args['humidity']:
            result.humidity = args['humidity']
        if args['visibility']:
            result.visibility = args['visibility']
        if args['predictability']:
            result.predictability = args['predictability']

        db.session.commit()

        return result

    def post(self, country_id):
        # args = weather_conditions_args.parse_args()
        result = WeatherModel.query.filter_by(id=country_id).first()
        if not result:
            abort(404, message="This country ID not found...")
        the_temp = result.the_temp
        return {"average_temperature": the_temp}

api.add_resource(Weather, "/weather/<int:country_id>")

if __name__=="__main__":
    db.create_all()
    app.run(debug=True)