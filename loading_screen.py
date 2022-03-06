import arcade
import arcade.gui
from basic_GUI import *

from arcade import load_texture
from arcade.gui import UIManager
from arcade.gui.widgets import UITextArea, UIInputText, UITexturePane

class LoadingView(arcade.View):

    def __init__(self):
        self.color = [200,50,50]
        self.last_max = 0
        super().__init__()
        arcade.set_background_color(arcade.color.ALMOND)
        self.manager = arcade.gui.UIManager()
        self.manager.enable()

        # BoxGroup Layout
        self.v_box = arcade.gui.UIBoxLayout()

        # Create a text label
        ui_text_label = arcade.gui.UITextArea(text="ABC ATCS Freshman Sim", x = 200, y = 500,
                                              width=450,
                                              height=40,
                                              font_size=20,
                                              font_name="Kenney Future")
        self.manager.add(ui_text_label.with_space_around(bottom=0))
        ui_text_label = arcade.gui.UITextArea(text="Pre-Release 2.0.1", x = 200, y = 400,
                                              width=450,
                                              height=40,
                                              font_size=20,
                                              font_name="Kenney Future")
        self.manager.add(ui_text_label.with_space_around(bottom=0))


        # UITextureButton
        texture = arcade.load_texture(":resources:onscreen_controls/flat_dark/play.png")
        ui_texture_button = arcade.gui.UITextureButton(texture=texture)

        # assign self.on_click_start as callback
        ui_texture_button.on_click = self.on_click_start
        self.v_box.add(ui_texture_button.with_space_around(bottom=20))

        self.manager.add(
            arcade.gui.UIAnchorWidget(
                anchor_x="center_x",
                anchor_y="center_y",
                child=self.v_box)
        )

        # instructions = '''
        # enter stuff here
        # '''

        # bg_tex = load_texture(":resources:gui_basic_assets/window/grey_panel.png")
        # text_area = UITextArea(x=100,
        #                        y=200,
        #                        width=200,
        #                        height=300,
        #                        text=instructions,
        #                        text_color=(0, 0, 0, 255))
        # self.manager.add(
        #     UITexturePane(
        #         text_area.with_space_around(right=20),
        #         tex=bg_tex,
        #         padding=(10, 10, 10, 10)
        #     )
        # )

        # self.manager.add(
        #     UITexturePane(
        #         UIInputText(x=340, y=200, width=200, height=50, text="Hello"),
        #         tex=bg_tex,
        #         padding=(10, 10, 10, 10)
        #     ))
        # self.manager.add(
        #     UIInputText(x=340, y=110, width=200, height=50, text="Hello"),
        # )
    
    def on_click_start(self, event):
        game_view = GameView()
        self.window.show_view(game_view)
        self.manager.remove(self.v_box)
    
    def on_draw(self):
        self.clear()
        self.manager.draw()
    def on_update(self,event):
        arcade.set_background_color((self.color[0],self.color[1],self.color[2]))
        if self.color[self.last_max] > 50:
            self.color[self.last_max] -=2
        if self.color[((self.last_max+1) % 3)] <200:
            self.color[((self.last_max+1) % 3)] += 2
        else:
            self.last_max +=1
            self.last_max %=3