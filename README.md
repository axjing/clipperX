# JANClipper

JANClipper自动生成视频字幕，可筛选视频片段自动剪辑。

## 使用方法

### 转录视频生成 `.srt` 和 `.md` 文件的字幕

```bash
python main.py -t test_video.mp4
```

1. 如果对转录质量不满意，可以使用更大的模型，例如

```bash
python main.py -t test_video.mp4 --whisper-model large
```

默认是 `small`。更好的模型是 `medium` 和 `large`，但推荐使用 GPU 获得更好的速度。也可以使用更快的 `tiny` 和 `base`，但转录质量会下降。


### 剪切视频

```bash
python main.py -c test_video.mp4 test_video.srt test_video.md # 默认视频比特率是 `--bitrate 10m`，你可以根据需要调大调小。
```
1. 如果不习惯 Markdown 格式文件，你也可以直接在 `srt` 文件里删除不要的句子，在剪切时不传入 `md` 文件名:
```bash
python main.py -c test_video.mp4 test_video.srt
```
2. 如果仅有 `srt` 文件，编辑不方便可以使用如下命令生成 `md` 文件，然后编辑 `md` 文件即可，但此时会完全对照 `srt` 生成，不会出现 `no speech` 等提示文本。
```bash
python main.py -m test.srt test.mp4
python main.py -m test.mp4 test.srt # 支持视频和字幕乱序传入
python main.py -m test.srt # 也可以只传入字幕文件
```
3. 编辑更新生成更新的字幕 `test_video_edited.srt`;
```bash
python main.py -s test_video.md test_video.srt
```
4. 解决 `srt` 里面空行太多。你可以使用 `python main.py -s test_video.srt` 来生成一个紧凑些的版本 `test_video_compact.srt` 方便编辑，编辑完成后，`python main.py -s test_video_compact.srt` 转回正常格式。
5. 如果输出的乱码
python main.py 默认输出编码是 `utf-8`. 确保你的编辑器也使用了 `utf-8` 解码。你可以通过 `--encoding` 指定其他编码格式。但是需要注意生成字幕文件和使用字幕文件剪辑时的编码格式需要一致。例如使用 `gbk`。
```bash
python main.py -t test.mp4 --encoding=gbk
python main.py -c test.mp4 test.srt test.md --encoding=gbk
```


## 参考项目
- [Whisper](https://github.com/openai/whisper.git)
- [autocut](https://github.com/mli/autocut.git)