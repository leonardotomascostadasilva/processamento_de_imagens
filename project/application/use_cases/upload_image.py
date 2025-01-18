from PIL import Image
import io
from domain.models import ImageModel
from sqlalchemy.orm import Session

class UploadImageUseCase:
    def __init__(self, session: Session):
        self.session = session

    def execute(self, file, context: str = None):
        if not file.filename.lower().endswith('.tif'):
            raise ValueError("Apenas arquivos .tif são aceitos")
        
        try:
            img = Image.open(file)
            img_buffer = io.BytesIO()
            img.save(img_buffer, format="TIFF")
            img_buffer.seek(0)

            new_image = ImageModel(name=file.filename, image_data=img_buffer.read(), context=context)
            self.session.add(new_image)
            self.session.commit()
            return f"Imagem '{file.filename}' armazenada com sucesso!"
        except Exception as e:
            self.session.rollback()
            raise e
