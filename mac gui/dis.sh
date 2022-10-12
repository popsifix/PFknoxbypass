  ./adb shell "pm disable-user --user 0 com.sec.enterprise.knox.cloudmdm.smdms"
	./adb shell "pm disable-user --user 0 com.samsung.android.knox.analytics.uploader"
	./adb shell "pm disable-user --user 0 com.samsung.android.knox.attestation"
	./adb shell "pm disable-user --user 0 com.samsung.knox.keychain"
	./adb shell "pm disable-user --user 0 com.samsung.android.knox.pushmanager"
	./adb shell "pm disable-user --user 0 com.samsung.android.knox.kpecore"
	./adb shell "pm enable com.knox.vpn.proxyhandler"
  ./adb shell "pm disable-user --user 0 com.samsung.android.kgclient"
    ./adb shell "pm disable-user --user 0 com.samsung.android.bbc.bbcagent"
    ./adb shell "pm disable-user --user 0 com.samsung.android.mdm"
    ./adb shell "pm disable-user --user 0 com.samsung.android.mdagent"
    ./adb shell "pm enable com.samsung.ssu"
  #./adb shell "pm disable-user --user 0 com.android.phone"
    ./adb shell "pm disable-user --user 0 com.sec.epdgtestapp"
    ./adb shell "pm disable-user --user 0 com.sec.epdg"
    ./adb shell "pm disable-user --user 0 com.samsung.klmsagent"


#setup
	#./adb shell "pm disable-user --user 0 com.google.android.setupwizard"
    #./adb shell "pm disable-user --user 0 com.sec.android.app.setupwizard"
     ./adb reboot