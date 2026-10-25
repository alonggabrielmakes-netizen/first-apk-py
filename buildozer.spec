[app]

# (str) Title of your application
title = MyKivyApp

# (str) Package name
package.name = mykivyapp

# (str) Package domain (needed for android/ios packaging)
package.domain = org.myapp

# (str) Source code where the main.py is located
source.dir = .

# (list) List of inclusions using pattern matching
source.include_exts = py,png,jpg,jpeg,kv,atlas

# (list) List of directory to include
source.include_dirs = 

# (str) Application versioning
version = 0.1

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientation
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (str) Presplash of the application
presplash.filename = 

# (str) Icon of the application
icon.filename = 

# (str) Name of the APK to build
apk.name = 

# (str) The Android arch to build for
android.archs = arm64-v8a,armeabi-v7a

# ✅ Auto-accept SDK license — THIS FIXES THE ERROR!
android.accept_sdk_license = True

# ✅ Use a known-good build tools version
android.buildtools = 34.0.0

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 20

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 0
