from flask import Flask, jsonify
from repository.database import db
from models.payment import Payment

app = Flask(__name__)

app.config['SECRET_KEY'] = "FLASK_SECRET_KEY"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:postgres@localhost:5434/module_cinco_websockets"

db.init_app(app)

@app.route('/payments/pix', methods=['POST'])
def create_payment_pix():
    return jsonify({
        "message": "The payment has been created"
    })

@app.route('/payments/pix/confirmation', methods=['POST'])
def pix_confirmation():
    return jsonify({
        "message": "The payment has been confirmed"
    })

@app.route('/payments/pix/<payment_id>', methods=['GET'])
def payment_pix_page(payment_id):
    return "pagamento pix"

if __name__ == "__main__":
    app.run(debug=True)