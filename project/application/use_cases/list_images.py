from domain.models import ImageModel
from sqlalchemy.orm import Session

class ListImagesByContextUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, context: str):
        query = self.session.query(ImageModel)
        
        if context:
            query = query.filter(ImageModel.context == context)
        
        images = query.all()
        return [
            {
                "id": image.id,
                "name": image.name,
                "context": image.context,
                "created_at": image.created_at.isoformat() if image.created_at else None
            }
            for image in images
        ]
