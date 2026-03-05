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
                image_url="https://images.unsplash.com/photo-1535930891776-0c2dfb7fda1a?auto=format&fit=crop&q=80&w=800"
            ),
            Product(
                name="VitaSmooth Portable Blender",
                description="Power through your day with fresh smoothies anywhere. USB rechargeable, high-torque motor, and sleek design for the modern wellness enthusiast.",
                price=45.50,
                image_url="https://images.unsplash.com/photo-1570222094114-d054a817e56b?auto=format&fit=crop&q=80&w=800"
            ),
            Product(
                name="GlowFlow LED Cloud Ceiling Lamp",
                description="Transform your space with atmospheric lighting. Smart app control, millions of colors, and a unique floating aesthetic for a futuristic home vibe.",
                price=119.00,
                image_url="https://images.unsplash.com/photo-1540932239986-30128078f3c5?auto=format&fit=crop&q=80&w=800"
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
