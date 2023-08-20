from diffusers import DiffusionPipeline
import os
current_path=os.path.dirname(__file__)
ckpt_path=os.path.join(current_path,"../caches/ckpt")
# print(ckpt_path)
def text2im_api(prompt):
    model_id_or_path = "CompVis/ldm-text2im-large-256"
    # model_id_or_path = "runwayml/stable-diffusion-v1-5"
    d_pipe = DiffusionPipeline.from_pretrained(model_id_or_path,cache_dir=ckpt_path)
    # pipeline.to("cuda")
    d_pipe.safety_checker = lambda images, clip_input: (images, False)
    im=d_pipe(prompt).images[0]
    return im