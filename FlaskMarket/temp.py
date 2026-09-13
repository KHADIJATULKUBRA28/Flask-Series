from market import db, app
from market.models import Item

with app.app_context():
    db.create_all()
    item1 = Item(name="iPhone 18", price=2000, barcode='797239742979', description='The best phone in the world')
    item2 = Item(name="Samsung S30 Ultra", price=1500, barcode='797239742989', description='The best Samsung phone ever made')
    item3 = Item(name="iPhone 20", price=2000, barcode='797239742999', description='The latest and greatest iPhone')
    db.session.add(item1)
    db.session.add(item2)
    db.session.add(item3)
    db.session.commit()