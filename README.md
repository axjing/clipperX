# AIClipper


JANClipper自动生成视频字幕。然后你选择需要保留的句子，对你视频中对应的片段裁切并保存。你无需使用视频编辑软件，只需要编辑文本文件即可完成剪切。

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


1. 讲得流利的视频的转录质量会高一些，这因为是 Whisper 训练数据分布的缘故。对一个视频，你可以先粗选一下句子，然后在剪出来的视频上再剪一次。
2. ~~最终视频生成的字幕通常还需要做一些小编辑。你可以直接编辑`md`文件（比`srt`文件更紧凑，且嵌入了视频）。然后使用 `autocut -s 22-52-00.md 22-52-00.srt` 来生成更新的字幕 `22-52-00_edited.srt`。注意这里会无视句子是不是被选中，而是全部转换成 `srt`。~~
3. 最终视频生成的字幕通常还需要做一些小编辑。但 `srt` 里面空行太多。你可以使用 `autocut -s 22-52-00.srt` 来生成一个紧凑些的版本 `22-52-00_compact.srt` 方便编辑（这个格式不合法，但编辑器，例如 VS Code，还是会进行语法高亮）。编辑完成后，`autocut -s 22-52-00_compact.srt` 转回正常格式。
4. 用 Typora 和 VS Code 编辑 Markdown 都很方便。他们都有对应的快捷键 mark 一行或者多行。但 VS Code 视频预览似乎有点问题。
5. 视频是通过 ffmpeg 导出。在 Apple M1 芯片上它用不了 GPU，导致导出速度不如专业视频软件。

1. **输出的是乱码？**

   AutoCut 默认输出编码是 `utf-8`. 确保你的编辑器也使用了 `utf-8` 解码。你可以通过 `--encoding` 指定其他编码格式。但是需要注意生成字幕文件和使用字幕文件剪辑时的编码格式需要一致。例如使用 `gbk`。

    ```bash
    autocut -t test.mp4 --encoding=gbk
    autocut -c test.mp4 test.srt test.md --encoding=gbk
    ```

    如果使用了其他编码格式（如 `gbk` 等）生成 `md` 文件并用 Typora 打开后，该文件可能会被 Typora 自动转码为其他编码格式，此时再通过生成时指定的编码格式进行剪辑时可能会出现编码不支持等报错。因此可以在使用 Typora 编辑后再通过 VSCode 等修改到你需要的编码格式进行保存后再使用剪辑功能。

## 参考项目
- [Whisper](https://github.com/openai/whisper.git)
- [autocut](https://github.com/mli/autocut.git)