import matplotlib.pyplot as plt
from shinyswatch import theme
import numpy as np
import pandas as pd
from shiny import App, render, ui, reactive

theme.darkly()
#icon=icon_svg("play"), class_="btn-primary"
# Here is where I will add in the items
app_ui = ui.page_fluid(  
        ui.page_navbar(
            ui.nav_spacer(),
            ui.nav_control(ui.input_action_button(id="about_modal", label="About",class_="btn-primary")),
            #ui.input_action_link("about", "About"),
            #ui.nav_panel("A", "Page A content"),  
            #ui.nav_panel("B", "Page B content"),  
            #ui.nav_panel("C", "Page C content"),  
            title="Smart Heal Treatmant Plan Prototype",  
            id="treatment_selection",
        ), 
        ui.layout_sidebar(
            ui.sidebar(
                ui.input_select(  
                    id="first_option",
                    label="Select an option below:",  
                    choices={"AA":"None Selected","1A": "Choice 1A", "1B": "Choice 1B", "1C": "Choice 1C"}, 
                    selected="AA",   
                ),
                ui.input_select(  
                    id="second_option",  
                    label="Select an option below:",  
                    choices={"AA":"None Selected","1A": "Choice 1A", "1B": "Choice 1B", "1C": "Choice 1C"},  
                    selected="AA",  
                ),
                ui.input_select(  
                    id="third_option", 
                    label="Select an option below:",  
                    choices={"AA":"None Selected","1A": "Choice 1A", "1B": "Choice 1B", "1C": "Choice 1C"},  
                    selected="AA",  
                ),
        ),

        ui.output_data_frame("treatment_plan"),
    ),
)  

def server(input, output, session):
    @render.data_frame  
    def treatment_plan():
        treatment_plan = pd.DataFrame()
        if not (input.first_option() == 'AA' or input.second_option() == 'AA' or input.third_option() == 'AA'):
            treatment_plan =  pd.DataFrame([{'Application Order':1,'Treatment':input.first_option()},
                                            {'Application Order':2,'Treatment':input.second_option()},
                                            {'Application Order':3,'Treatment':input.third_option()}])

        return render.DataGrid(treatment_plan) 
    
    @reactive.effect
    @reactive.event(input.about_modal,ignore_none=True)
    def _():
        m = ui.modal(
            ui.h3("Contributors and Information"),
            ui.h5("Smart Heal Prototype Contributors"),
            ui.TagList(ui.div("Matthew May"),ui.div("Nidhi"),ui.div('Yash')),
            size="l",
            easy_close=True,
            footer=None,
        )
        ui.modal_show(m)

app = App(app_ui, server,debug=True)
