from ..models import ImgMri
from examenes.models import Examen

def get_imgmris():
    queryset = ImgMri.objects.all()
    return (queryset)

def create_imgmris(form):
    measurement = form.save()
    measurement.save()
    return ()

def cargarPrueba():
    examenes = [
    "sub-00001_T1",
    "sub-00001_T2",
    "sub-00001_T3"
    ]
    BASE_GITHUB_URL = "https://raw.githubusercontent.com/sofiaghost/MRI-Archivos/main/examen_1/"

    """Crea registros en la BD con URLs de imágenes en GitHub."""
    imagenes=ImgMri.objects.all()
    if len(imagenes)==0:
        examen = Examen.objects.get_or_create(solicitud=1, paciente="sub-00001", cc=123456, fecha="2021-01-01")[0]

        for folder in examenes:

            for i in range(100):  # Suponiendo que cada folder tiene 100 imágenes
                image_url = f"{BASE_GITHUB_URL}{folder}/slice_{i:03d}.png"
                # Intentar guardar la imagen en la base de datos
                ImgMri.objects.create(examen=examen, url=image_url)
    return ()
