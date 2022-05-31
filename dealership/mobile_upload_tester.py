from dealership.models import Car
from dealership.mobile_upload.upload import MobileUploader


car = Car.objects.all()[0]
uploader = MobileUploader(car)
uploader.run()

# exec(open('dealership/mobile_upload_tester.py').read())
# C:\Users\Yavor\Desktop\CarDealershipBackend\manage.
