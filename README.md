# JANClipper

JANClipper自动生成视频字幕，可筛选视频片段自动剪辑。

## 使用方法
```
python main.py test_video.mp4 --cfg=config
```
其中config内容包括
```yaml
# ./caches/config.yaml
encoding: UTF-8     # 默认输出编码是 `utf-8`. 确保你的编辑器也使用了 `utf-8` 解码。你可以通过 `--encoding` 指定其他编码格式。但是需要注意生成字幕文件和使用字幕文件剪辑时的编码格式需要一致。例如使用 `gbk`。
device: cpu         # choices=["cpu", "cuda"]
use_VAD: auto       # ["1", "0", "auto"] If or not use VAD"
force_write: False  #  Force write even if files exist
bitrate: 10m        # The bitrate to export the cutted video, such as 10m, 1m, or 500k 默认视频比特率是 `--bitrate 10m`，你可以根据需要调大调小
prompt: Hello       # initial prompt feed into whisper
whisper_model: tiny # choices=["tiny", "base", "small", "medium", "large", "large-v2"]  help="The whisper model used to transcribe." 默认是 `small`。更好的模型是 `medium` 和 `large`，但推荐使用 GPU 获得更好的速度。也可以使用更快的 `tiny` 和 `base`，但转录质量会下降。
language: zh        # choices=["zh", "en"], help="The output language of transcription"
cut_mode: cut       # choices=["transcribe","cut", "daemon","to_md","srt_to_compact"],
                        # transcribe 转录视频生成 `.srt` 和 `.md` 文件的字幕
                        # cut 如果不习惯 Markdown 格式文件，你也可以直接在 `srt` 文件里删除不要的句子，在剪切时不传入 `md` 文件名
                        # to_md 如果仅有 `srt` 文件，编辑不方便可以使用如下命令生成 `md` 文件，然后编辑 `md` 文件即可，但此时会完全对照 `srt` 生成，不会出现 `no speech` 等提示文本。
                        # srt_to_compact 解决 `srt` 里面空行太多。你可以使用 `python main.py -s test_video.srt` 来生成一个紧凑些的版本 `test_video_compact.srt` 方便编辑，编辑完成后，`python main.py -s test_video_compact.srt` 转回正常格式。
```
### 操作步骤
1. 设置`./caches/config.yaml`中配置参数
2. 设置`./caches/config.yaml`中配置参数**cut_mode: transcribe** ，识别视频字幕，并保存字幕为`.srt` 和 `.md`
```
python main.py E:\ArtLife\JVideoClips\202112052123.mp4 --cfg=config
```
3. 从识别的字幕中删除需要剪辑掉的的字幕
4. 设置`./caches/config.yaml`中配置参数**cut_mode: cut** ，识别视频字幕，并保存字幕为`.srt` 和 `.md`
```
python main.py E:\ArtLife\JVideoClips\202112052123.mp4 --cfg=config
```
## 常见问题
### ffmpeg未安装
```sh
scoop install ffmpeg    # for win
```
并将`C:\Users\xxxx\scoop\apps\ffmpeg\6.0\bin`添加到环境变量

其他系统一样

## 参考项目
- [Whisper](https://github.com/openai/whisper.git)
- [autocut](https://github.com/mli/autocut.git)