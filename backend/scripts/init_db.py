import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.db import Base, engine
from app.models import models

print("Creating tables...")
Base.metadata.create_all(bind=engine)
print("Done.")