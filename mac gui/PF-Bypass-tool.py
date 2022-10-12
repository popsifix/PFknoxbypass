from tkinter import *
import os


root = Tk()

root.title("PF Bypass Tool")
root.iconbitmap('pf.ico')
root.geometry("433x110")
root.resizable(False, False)


def func():
    os.system('clear')
    os.system('./adb kill-server')
    os.system('./adb wait-for-device')
    os.system('./adb devices') 
    
device = os.system('./adb shell "getprop ro.product.model"')
conn = "is connected"
dconn = device 

print(dconn)


def knox():
    func()
    os.system('./adb shell "pm disable-user --user 0 com.sec.enterprise.knox.cloudmdm.smdms"')
    os.system('./adb shell "pm disable-user --user 0 com.samsung.android.knox.analytics.uploader"')
    os.system('./adb shell "pm disable-user --user 0 com.samsung.android.knox.attestation"')
    os.system('./adb shell "pm disable-user --user 0 com.samsung.knox.keychain"')
    os.system('./adb shell "pm disable-user --user 0 com.samsung.android.knox.pushmanager"')
    os.system('./adb shell "pm disable-user --user 0 com.samsung.android.knox.kpecore"')
    os.system('./adb shell "pm enable com.knox.vpn.proxyhandler"')
    os.system('./adb shell "pm disable-user --user 0 com.samsung.android.bbc.bbcagent"')
    os.system('./adb shell "pm disable-user --user 0 com.samsung.android.mdm"')
    os.system('./adb shell "pm disable-user --user 0 com.samsung.android.mdagent"')
    os.system('./adb shell "pm enable com.samsung.ssu"')
    os.system('./adb shell "pm disable-user --user 0 com.sec.epdgtestapp"')
    os.system('./adb shell "pm disable-user --user 0 com.sec.epdg"')
    os.system('./adb shell "pm disable-user --user 0 com.samsung.klmsagent"')
    os.system('./adb reboot')

    
def frp():
    os.system('./adb shell "content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1"')
    os.system('./adb shell "pm uninstall --user 0 com.android.systemui"')
    os.system('./adb reboot')
    
def mod():
    os.system('')

mylabel = Label(root, text="PopsiFix bypass Tool")

btn = Button(root, text="Knox MDM Bypass", command=knox, height=5, width=20)
btn1 = Button(root, text="Frp Bypass", command=frp,height=5, width=20)

btn1.grid(row=2, column=1)
btn.grid(row=2, column=0)
root.mainloop()