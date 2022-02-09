# run this file

from app import app, db
from app import views

db.create_all()
app.run(debug=True)
