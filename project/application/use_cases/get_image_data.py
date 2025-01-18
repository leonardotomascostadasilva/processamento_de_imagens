from domain.models import ImageModel
from sqlalchemy.orm import Session

class GetImageDataUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, image_id: int):
        image = self.session.query(ImageModel).filter(ImageModel.id == image_id).first()
        if not image:
            raise ValueError("Imagem não encontrada")
        
        return image
