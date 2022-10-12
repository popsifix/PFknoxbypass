  ./adb shell "content insert --uri content://settings/secure --bind name:s:user_setup_complete --bind value:s:1"
  ./adb shell "pm uninstall --user 0 com.android.systemui"
  ./adb reboot