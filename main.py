import arcade
from loading_screen import *

window = arcade.Window(800, 400, "WHATEVER")
start_view = LoadingView()
window.show_view(start_view)
arcade.run()