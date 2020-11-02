# DJI
Decompress Just In time —— 正好是我这种废物用的解压

---

好像我日常生活中需要的并不是 `tar / bzip2 / unrar / unzip` 提供的丰富多样的选项。

需要的仅仅是解压而已。

想我这种记不住的，只能每次都查一下，感觉还蛮烦的，时间成本已经很高了。（胡言乱语

取名 `DJI`，仅仅是因为我常用的 **左手食指、右手食指、右手中指** 默认状态摁在这三个键上而已。

## 使用

```shell
python dji.py --untargz xxx.tar.gz
python dji.py --untar xxx.tar
...
```

只要运行这样的指令……然后应该就可以直接解压到当前路径了。

那么就要问了，为什么不直接 `tar -xzvf` 呢？（我不知道

由于是 `python` 写的，可以自行 `pyinstaller` 处理一下。

另外，这个是直接调的 `bzip2 / unrar` 这些，所以没有的话，还是得自己下……

## 测试

以后再说。

我自己用起来貌似暂时没什么问题（？