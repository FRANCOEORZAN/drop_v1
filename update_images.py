from app import app
from models import db, Product

def update_images():
    with app.app_context():
        # Update mappings
        updates = {
            "PawGuard No-Pull Dog Harness": "/static/img/dog_harness.png",
            "Aura Interactive Cat Laser": "/static/img/cat_laser.png",
            "ZenCalm Orthopedic Pet Bed": "/static/img/orthopedic_pet_bed.png",
            "AquaPaws Portable Water Bottle": "/static/img/pet_water_bottle.png",
            "MudMaster Automatic Paw Cleaner": "/static/img/paw_cleaner.png",
            "SmartFeeds Wifi Auto-Feeder": "/static/img/smart_pet_feeder.png"
        }
        
        for name, url in updates.items():
            product = Product.query.filter_by(name=name).first()
            if product:
                product.image_url = url
                print(f"Updated image for {product.name}")
        
        db.session.commit()
        print("Database updated successfully.")

if __name__ == "__main__":
    update_images()
