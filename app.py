
import gradio as gr
from functools import partial
from get_similar_program import search_programs
from get_insights import get_insights
import pandas as pd
import threading

title = "AI Sales Whisperer demo 🛫"
desc = "AI copilot to help sales persons to close deals more quickly - Medium article on how it works: LINK"

with gr.Blocks(title=title) as demo:
    gr.Markdown(f"# {title}")
    with gr.Row():
        with gr.Column(scale=8):
            gr.Markdown("**"+desc+"**")
        with gr.Column(scale=2):
            copilot_button = gr.Button(value="Run Whisperer (REAL TIME)",)
            
            
    with gr.Row():
        with gr.Column(scale=2):
            with gr.Row():
                fig = gr.Plot()
            with gr.Row():
                status = gr.Markdown("## Lead status",)
        with gr.Column(scale=5):
            gr.Markdown("## Program Catalog [Available in French]")
            with gr.Accordion("Manual Search", open=False):
                text_area = gr.Textbox(placeholder="Write here", lines=3, label="Describe what you are looking for")
                with gr.Column(scale = 2):
                    search_button = gr.Button(value="Find Programs")                
                with gr.Column(scale=1):
                    number_to_display = gr.Number(value=10,label = "Number of programs to display")    
            with gr.Accordion("All results:"):
                ll = gr.Markdown("Empty")
    search_function = partial(search_programs)
    copilot_fn = partial(get_insights)

    copilot_button.click(fn = copilot_fn, inputs = [], outputs=[fig, status, ll] ,show_progress="minimal")
    search_button.click(fn=search_function, inputs=[text_area,number_to_display], outputs=[ll],show_progress="minimal")
    
demo.launch(max_threads=40, show_error=True)
