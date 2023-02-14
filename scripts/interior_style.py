# -*- coding: utf-8 -*-
# @Time : 2023/2/14 12:03 下午
# @Author : *
# @Email : *@tezign.com
# @Desc :

from modules import scripts, shared
import gradio as gr


interior_type = ["None", "Living room", "Bedroom", "Kitchen", "Bath room", "Dining room", "Walk in closet", "Home office",
                 "Outdoor pool area", "Outdoor patio", "Outdoor garden", "Gaming room", "Attic", "Meeting room",
                 "Workshop", "Study room", "Coworking space", "Exhibition space", "Office", "Fitness gym", "Coffee shop",
                 "Clothing store", "Restaurant", "Onsen", "Hotel lobby", "Hotel room", "Hotel bathroom", "Toilet"]
interior_style = ["None", "Modern", "Minimalist", "Scandinavian", "Zen", "Art nouveau", "Industrial", "Neoclassic",
                  "Japanese design", "Contemporary", "Vintage", "Maximalist", "Art deco", "Bohemian", "Cyberpunk",
                  "Interior AI", "Sketch", "Biophilic", "Cottagecore", "Farmhouse", "Rustic", "Tropical", "Coastal",
                  "Ski chalet", "Tribal", "Vaporwave", "Halloween", "Christmas", "Midcentury Modern", "Medieval",
                  "Gothic", "Baroque", "French country"]


class InteriorScript(scripts.Script):

    # The title of the script. This is what will be displayed in the dropdown menu.
    def title(self):
        return "Fast Interior Design Style"

    # Determines when the script should be shown in the dropdown menu via the
    # returned value. As an example:
    # is_img2img is True if the current tab is img2img, and False if it is txt2img.
    # Thus, return is_img2img to only show the script on the img2img tab.
    def show(self, is_img2img):
        return scripts.AlwaysVisible

    # How the script's is displayed in the UI. See https://gradio.app/docs/#components
    # for the different UI components you can use and how to create them.
    # Most UI components can return a value, such as a boolean for a checkbox.
    # The returned values are passed to the run method as parameters.
    def ui(self, is_img2img):
        with gr.Group():
            with gr.Accordion("Interior Styles", open=False):
                type_ratio = gr.Dropdown(label='interior-type', choices=interior_type, value="None")
                style_ratio = gr.Dropdown(label='interior-style ', choices=interior_style, value="None")

        return [type_ratio, style_ratio]

    """
    This function is called before processing begins for AlwaysVisible scripts.
    You can modify the processing object (p) here, inject hooks, etc.
    args contains all values returned by components from ui()
    """
    def process(self, p, type_ratio, style_ratio):
        prompt = p.all_prompts[0]
        # remember change p.all_prompts[]
        if type_ratio != 'None':
            prompt = type_ratio + ', ' + prompt

        if style_ratio != 'None':
            prompt = style_ratio + ', ' + prompt

        p.prompt = prompt
        p.all_prompts[0] = prompt

