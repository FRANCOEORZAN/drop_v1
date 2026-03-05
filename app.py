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
                name="Midnight Chronograph",
                description="A sleek, minimalist timepiece featuring a matte black dial and a premium leather strap. Perfect for both formal and casual settings.",
                price=149.99,
                image_url="https://images.unsplash.com/photo-1523275335684-37898b6baf30?auto=format&fit=crop&q=80&w=800"
            ),
            Product(
                name="Aura Wireless Earbuds",
                description="High-fidelity sound meets striking aesthetic. Active noise cancellation and an ergonomic design for all-day comfort.",
                price=89.50,
                image_url="https://images.unsplash.com/photo-1590658268037-6bf12165a8df?auto=format&fit=crop&q=80&w=800"
            ),
            Product(
                name="Obsidian Desk Mat",
                description="Elevate your workspace with this premium faux-leather desk pad. Offers a smooth gliding surface and protects your desk in style.",
                price=34.00,
                image_url="https://images.unsplash.com/photo-1527443154391-507e9dc6c5cc?auto=format&fit=crop&q=80&w=800"
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
