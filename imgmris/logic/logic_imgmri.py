from ..models import ImgMri

def get_imgmris():
    queryset = ImgMri.objects.all()
    return (queryset)

def create_imgmris(form):
    measurement = form.save()
    measurement.save()
    return ()