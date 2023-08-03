# -*- coding: utf-8 -*-
import gradio as gr
import os
from common.yaml_parser import YamlParser
from common.utils import read_file

CURRENT_DIR=os.path.dirname(__file__)

transcribe_config_path=os.path.join(CURRENT_DIR,"caches/transcribe_config")

def transcriber_web_api(video_path,audio_path,yaml_file=transcribe_config_path):
    print(transcribe_config_path)
    args = YamlParser(cfg_name="", path=yaml_file)#.add_args(args)
    if video_path:
        file_path=video_path
    elif audio_path:
        file_path=audio_path
    else:
        print("EEOR")
    
        
    args.inputs=[file_path]

    from cores.transcriber import Transcribe
    
    srt_o=Transcribe(args).run()
    
    srt_file=os.path.splitext(file_path)[0]+".srt"
    
    txt=read_file(srt_file)
    
    return txt

demo=gr.Interface(
    fn=transcriber_web_api,
    inputs=[gr.Video(source="upload", label="In",interactive=True),
            gr.Audio(source="upload", label="In",type="filepath", interactive=True)],
    outputs="text",
    css="footer {visibility: hidden}",
)

if __name__ == "__main__":
    demo.launch(share=False)

