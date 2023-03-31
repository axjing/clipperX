# AIClipper


AIClipper自动生成视频字幕。然后你选择需要保留的句子，对你视频中对应的片段裁切并保存。你无需使用视频编辑软件，只需要编辑文本文件即可完成剪切。
## 使用方法

### 转录某个视频生成 `.srt` 和 `.md` 结果。

```bash
autocut -t 22-52-00.mp4
```

1. 如果对转录质量不满意，可以使用更大的模型，例如

```bash
autocut -t 22-52-00.mp4 --whisper-model large
```

默认是 `small`。更好的模型是 `medium` 和 `large`，但推荐使用 GPU 获得更好的速度。也可以使用更快的 `tiny` 和 `base`，但转录质量会下降。


### 剪切某个视频

```bash
autocut -c 22-52-00.mp4 22-52-00.srt 22-52-00.md
```

1. 默认视频比特率是 `--bitrate 10m`，你可以根据需要调大调小。
2. 如果不习惯 Markdown 格式文件，你也可以直接在 `srt` 文件里删除不要的句子，在剪切时不传入 `md` 文件名即可。就是 `autocut -c 22-52-00.mp4 22-52-00.srt`
3. 如果仅有 `srt` 文件，编辑不方便可以使用如下命令生成 `md` 文件，然后编辑 `md` 文件即可，但此时会完全对照 `srt` 生成，不会出现 `no speech` 等提示文本。

```bash
autocut -m test.srt test.mp4
autocut -m test.mp4 test.srt # 支持视频和字幕乱序传入
autocut -m test.srt # 也可以只传入字幕文件
```
