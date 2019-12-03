# from escpos.printer import Network
# from escpos.printer import Network
#
#
# all_devs = usb.core.find(find_all=True)
# for d in all_devs:
#     print(d.product)
#     if d.product == 'GP-58':
#         print(d.idVendor, d.idProduct, d)
#         # __init__(self, idVendor, idProduct, timeout=0, in_ep=0x82, out_ep=0x01, *args, **kwargs):
#         """ Seiko Epson Corp. Receipt Printer (EPSON TM-T88III) """
#         p = Usb(0x6868, 0x200, None, 0, 0x81, 0x2, profile="TM-T88III")
#         p.text("你好\n你好\n", chinese=True)
#         p.cut()
#         p.close()
#
# # 网络打印机
# kitchen = Network("192.168.123.100")  # Printer IP Address
# kitchen.text("Hello World\n")
# kitchen.barcode('1324354657687', 'EAN13', 64, 2, '', '')
# kitchen.cut()

# !/usr/bin/python
# -*- coding: UTF-8 -*-
# !/usr/bin/env python
# -*- coding: utf-8 -*-
import usb.util
from tkinter import *
import json

window = Tk()

window.title('USB打印助手')

window.geometry('500x300')  # 这里的乘是小x

# 本地usb设备列表
theLB = Listbox(window, selectmode=MULTIPLE, height=11, width=100)
theLB.pack()
usbDevices = []
all_devs = usb.core.find(find_all=True)
for d in all_devs:
    theLB.insert(END, d.product)
    usbDevices.append(d)


def callback():
    selected = theLB.curselection()
    usbConfigs = []
    for i in selected:
        d = usbDevices[i]
        usbConfigs.append({
            "name": d.product,
            "type": "usb",
            "address": "",
            "port": 9100,
            "idVendor": d.idVendor,
            "idProduct": d.idProduct,
            "timeout": 0,
            "in_ep": "111",
            "out_ep": "222"
        })

    # 读取json 把旧的usb device 删除 更换新的
    with open("config.json", 'r') as configfile:
        config = json.load(configfile)
        print(config)
        for printer in config['printers']:
            if printer['type'] == 'network':
                usbConfigs.append(printer)
        with open("config.json", "w") as f:

            config['printers'] = usbConfigs
            print('同步完成')
            json.dump(config, f)

theButton = Button(window, text='同步打印机数据', command=callback)
theButton.pack()

window.mainloop()
