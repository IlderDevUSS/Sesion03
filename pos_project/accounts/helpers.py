import uuid
import os

# Esta es una función placeholder. Necesitarás implementar la lógica real 
# para subir a AWS S3 o la ruta que uses en producción.
def photo_path_aws_instance(instance, filename):
    """Genera una ruta de almacenamiento única para la imagen del usuario."""
    ext = filename.split('.')[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    # Ruta de ejemplo: 'users/avatars/ID_DE_USUARIO/archivo.jpg'
    return os.path.join(f'users/avatars/{instance.username}', filename)