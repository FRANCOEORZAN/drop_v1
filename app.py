import os
from flask import Flask, render_template

from models import db, Product

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'instance', 'dropshipping.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Ensure the instance folder exists for the SQLite database
os.makedirs(os.path.join(basedir, 'instance'), exist_ok=True)

@app.route('/health')
def health():
    return {"status": "healthy"}, 200

# Auto-initialize and seed database
with app.app_context():
    db.create_all()
    if Product.query.count() == 0:
        sample_products = [
            Product(
                name="PawGuard No-Pull Dog Harness",
                description="The ultimate safety and comfort for your furry friend. Features reflective straps, breathable mesh, and a secure no-pull design for effortless walks.",
                price=29.99,
                image_url="/static/img/dog_harness.png"
            ),
            Product(
                name="Aura Interactive Cat Laser",
                description="Keep your cat entertained for hours with this automated laser toy. Features multiple speed modes and 360-degree rotation to stimulate natural hunting instincts.",
                price=24.50,
                image_url="/static/img/cat_laser.png"
            ),
            Product(
                name="ZenCalm Orthopedic Pet Bed",
                description="A premium memory foam bed designed to alleviate joint pain and provide deep, restful sleep. Features a removable, washable plush cover for easy care.",
                price=54.00,
                image_url="/static/img/orthopedic_pet_bed.png"
            ),
            Product(
                name="AquaPaws Portable Water Bottle",
                description="The essential travel companion for active pets. Integrates a leak-proof bottle with a built-in drinking bowl. Compact, one-handed operation for easy hydration on the go.",
                price=19.95,
                image_url="/static/img/pet_water_bottle.png"
            ),
            Product(
                name="MudMaster Automatic Paw Cleaner",
                description="Say goodbye to muddy footprints! This gentle silicone brush cleaner quickly and effectively removes dirt from paws before your pet steps back inside.",
                price=22.99,
                image_url="/static/img/paw_cleaner.png"
            ),
            Product(
                name="SmartFeeds Wifi Auto-Feeder",
                description="Manage your pet's diet from anywhere. Program meal schedules and portions via app. Features a built-in camera to check in on your pet during mealtime.",
                price=129.00,
                image_url="/static/img/smart_pet_feeder.png"
            )
        ]
        db.session.add_all(sample_products)
        db.session.commit()

@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = Product.query.get_or_404(product_id)
    return render_template('product.html', product=product)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5050))
    app.run(host='0.0.0.0', port=port, debug=True)
