[app]

# (An Required) Title of your application
title = Shivam Escape Aditi

# (An Required) Package name
package.name = shivamescapeaditi

# (An Required) Package domain (needed for android packaging)
package.domain = org.test

# (An Required) Source code directory
source.dir = .

# Source files to include (let Kivy/Pygame find your files)
source.include_exts = py,png,jpg,jpeg,ttf

# Application version
version = 0.1

# (An Required) Application requirements
# Pygame requirements for bootstrap build
requirements = python3,pygame

# (An Required) Supported orientations
orientation = portrait

# (An Required) Fullscreen mode
fullscreen = 1

# Android specific configurations
android.api = 33
android.minapi = 21
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 0
