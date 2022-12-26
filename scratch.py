# import EAN13 from barcode module
from barcode import EAN13
# import ImageWriter to generate an image file
from barcode.writer import ImageWriter
# import random number 
import random

# Make sure to pass the number as string
number = random.randint(111111111111,999999999999)
numberPassing = str(number)
# Now, let's create an object of EAN13 class and
# pass the number with the ImageWriter() as the
# writer
my_code = EAN13(numberPassing, writer=ImageWriter())
# Our barcode is ready. Let's save it.SAVE TO YOUR PATH
my_code.save("C:/xampp/htdocs/product/python-barcode-generator/barcode-result/barcodeImageResult-"+numberPassing)
