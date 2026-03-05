from app import app
from models import db, Product

def init_db():
    with app.app_context():
        # Create all database tables
        db.create_all()

        # Check if we already have products, if not add them
        if Product.query.count() == 0:
            products = [
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
            db.session.add_all(products)
            db.session.commit()
            print("Database initialized and populated with dummy products.")
        else:
            print("Database already populated.")

if __name__ == '__main__':
    init_db()
