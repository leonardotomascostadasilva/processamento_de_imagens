from sqlalchemy import Column, Integer, String, LargeBinary, DateTime
from datetime import datetime
from infrastructure.database import Base

class ImageModel(Base):
    __tablename__ = 'images'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    image_data = Column(LargeBinary)
    context = Column(String)
    created_at = Column(DateTime, default=datetime.now)
