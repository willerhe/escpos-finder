from escpos.printer import Usb
from escpos.printer import Network
import usb.util

all_devs = usb.core.find(find_all=True)
for d in all_devs:
    print(d.product)
    if d.product == 'GP-58':
        print(d.idVendor, d.idProduct, d)
        # __init__(self, idVendor, idProduct, timeout=0, in_ep=0x82, out_ep=0x01, *args, **kwargs):
        """ Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
        p = Usb(0x6868, 0x200, None, 0, 0x81, 0x2, profile="TM-T88III")
        p.text("你好\n你好\n", chinese=True)
        p.cut()
        p.close()

# 网络打印机
kitchen = Network("192.168.123.100")  # Printer IP Address
kitchen.text("Hello World\n")
kitchen.barcode('1324354657687', 'EAN13', 64, 2, '', '')
kitchen.cut()



