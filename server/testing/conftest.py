#!/usr/bin/env python3
import pytest
from app import app, db
from models import Plant

@pytest.fixture(autouse=True)
def setup_database():
    """Set up test database before each test and tear down after."""
    with app.app_context():

        db.create_all()
        
        Plant.query.delete()
        
        plants = [
            Plant(id=1, name="Aloe", image="https://example.com/aloe.jpg", price=10, is_in_stock=True),
            Plant(id=2, name="Cactus", image="https://example.com/cactus.jpg", price=15, is_in_stock=True),
        ]
        
        db.session.add_all(plants)
        db.session.commit()
        
        yield  
        
        db.session.remove()
        db.drop_all()