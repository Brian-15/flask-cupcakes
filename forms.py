from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import URL, NumberRange, InputRequired, Optional

class NewCupcakeForm(FlaskForm):
    """form for adding cupcakes"""

    flavor  = StringField("Flavor", validators=[InputRequired()])
    size    = SelectField("Size", validators=[InputRequired()],
                          choices=[("small", "Small"),
                                   ("medium", "Medium"),
                                   ("large", "Large"),
                                   ("massive", "Massive")])
    rating  = FloatField("Rating", validators=[InputRequired(), NumberRange(min=0, max=5)])
    image   = StringField("Image URL", validators=[Optional(), URL()])
