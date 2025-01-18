from flask import Blueprint, request, jsonify, send_file, abort
from infrastructure.database import get_session
from application.use_cases.upload_image import UploadImageUseCase
from application.use_cases.list_images import ListImagesByContextUseCase
from application.use_cases.get_image_data import GetImageDataUseCase
import io

routes = Blueprint('routes', __name__)

@routes.route('/upload', methods=['POST'])
def upload_image():
    session = get_session()
    use_case = UploadImageUseCase(session)

    if 'files' not in request.files:
        return "Nenhum arquivo foi enviado", 400

    file = request.files['files']
    context = request.form.get('context', None)

    try:
        result = use_case.execute(file, context)
        return result, 200
    except ValueError as e:
        return str(e), 400
    except Exception as e:
        return f"Erro ao processar ou salvar a imagem: {str(e)}", 500

@routes.route('/images', methods=['GET'])
def list_images():
    session = get_session()
    use_case = ListImagesByContextUseCase(session)

    context = request.args.get('context', None)

    try:
        images = use_case.execute(context)
        return jsonify(images), 200
    except Exception as e:
        return f"Erro ao buscar imagens: {str(e)}", 500

@routes.route('/images/<int:image_id>/data', methods=['GET'])
def get_image_data(image_id):
    session = get_session()
    use_case = GetImageDataUseCase(session)

    try:
        image = use_case.execute(image_id)

        return send_file(
            io.BytesIO(image.image_data),
            mimetype='image/tif',
            as_attachment=False,
            download_name=image.name
        )
    except ValueError:
        abort(404, description="Imagem não encontrada")
    except Exception as e:
        return f"Erro ao buscar a imagem: {str(e)}", 500
    
