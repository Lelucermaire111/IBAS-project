import os
from dbr import *

def ISBNScan(image_path):
        # 1.Initialize license.
        # The string "DLS2eyJvcmdhbml6YXRpb25JRCI6IjIwMDAwMSJ9" here is a free public trial license. Note that network connection is required for this license to work.
        # You can also request a 30-day trial license in the customer portal: https://www.dynamsoft.com/customer/license/trialLicense?product=dbr&utm_source=samples&package=python
        error = BarcodeReader.init_license("t0074oQAAAIh0oQAxrPAEF6fy4JrUW40CK05rdbGZU50N7x9D8KACYZD27XeEJVSAlr85QLDeGXjMdTvoLLvFPP9YnYTRkAmyAPmOItU=")

        if error[0] != EnumErrorCode.DBR_OK:
            print("License error: "+ error[1])

        # 2.Create an instance of Barcode Reader.
        dbr = BarcodeReader()

        # Replace by your own image path
        # image_path = "./images/test2.jpg"

        # 3.Decode barcodes from an image file.
        results = dbr.decode_file(image_path)

        # 4.Output the barcode text.
        barcode = -1
        if results != None:
            for res in results:
                print("Barcode "  + ":" + res.barcode_text)
                barcode = res.barcode_text
            return barcode
        else:
            print("No data detected.")
            return barcode
