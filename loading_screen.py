import arcade
import arcade.gui
from basic_GUI import *

class LoadingView(arcade.View):

    def __init__(self):
        super().__init__(800,600,'BCA Sim...Booting Up')
        arcade.set_background_color(arcade.color.ALMOND)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # BoxGroup Layout
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="BCA ATCS Freshman Sim", x = 200, y = 500,
                                              width=450,
                                              height=40,
                                              font_size=20,
                                              font_name="Kenney Future")
        self.manager.add(ui_text_label.with_space_around(bottom=0))

        # Create a UITextureButton
        texture = arcade.load_texture(":resources:onscreen_controls/flat_dark/play.png")
        ui_texture_button = arcade.gui.UITextureButton(texture=texture)
        # --- Method 2 for handling click events,
        # assign self.on_click_start as callback
        ui_texture_button.on_click = self.on_click_start
        self.v_box.add(ui_texture_button.with_space_around(bottom=20))

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )
    
    def on_click_start(self, event:arcade.gui.UIOnClickEvent):
        game_view = GameView()
        game_view.setup()
        self.window.show_view(game_view)
    
    def on_draw(self):
        self.clear()
        self.manager.draw()