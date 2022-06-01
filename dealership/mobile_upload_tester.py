from dealership.models import Car, CarImage
from dealership.mobile_upload.upload import MobileUploader
from pathlib import Path
import os

car = Car.objects.all()[0]
images = [os.path.join(Path(os.getcwd()).parent,"media",Path(str(image.image))) for image in CarImage.objects.select_related().filter(Car=car)]
# print(images)
uploader = MobileUploader()
uploader.run(car, images)

# exec(open('mobile_upload_tester.py').read())
# C:\Users\Yavor\Desktop\CarDealershipBackend\manage.py
