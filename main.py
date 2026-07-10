import os
from kivy.app import App
from kivy.uix.webview import WebView

class MyWebApp(App):
    def build(self):
        # இது உங்க index.html ஃபைலை ஆப்புக்குள்ள ஓபன் பண்ணும்
        browser = WebView(url=f"file://{os.path.abspath('index.html')}")
        return browser

if __name__ == "__main__":
    MyWebApp().run()
