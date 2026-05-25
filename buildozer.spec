title = Shivam Escape Aditi
package.name = shivamescapeaditi
package.domain = org.test

# Kivy/Pygame game ke liye source files include karna zaroori hai
source.include_exts = py,png,jpg,kv,atlas,wav,mp3

# Requirements mein kivy ko add karna zaroori hota hai agar aap pygame-menu ya kivy scripts use kar rahe hain. 
# Agar sirf pure pygame use kar rahe hain to dhyaan dein ki python3-pygame recipes buildozer support kare.
requirements = python3,kivy,pygame

orientation = portrait
fullscreen = 1

# Android API levels (Ye bohot zaroori hai GitHub Actions ke liye)
android.api = 33
android.minapi = 21
android.ndk = 25b
