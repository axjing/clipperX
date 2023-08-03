import gradio as gr

from cores.diffuser_interfaces import text2im_api

text2im_app=gr.Interface(fn=text2im_api,
                         inputs=[gr.Text(label="Prompt")],
                         outputs=[gr.Image(label="Out")],
                         css="footer {visibility: hidden}",)

if __name__=="__main__":
    text2im_app.launch(share=False)