<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/blob/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<div align="center">

# nonebot-plugin-wearskirt

_✨ NoneBot 赛博女装插件 ✨_

<a href="./LICENSE">
    <img src="https://img.shields.io/github/license/Lfhsheng/nonebot-plugin-wearskirt.svg" alt="license">
</a>
<a href="https://pypi.python.org/pypi/nonebot-plugin-wearskirt">
    <img src="https://img.shields.io/pypi/v/nonebot-plugin-wearskirt.svg" alt="pypi">
</a>
<img src="https://img.shields.io/badge/python-3.8+-blue.svg" alt="python">

</div>

作者代码水平不高，恳请各位大佬对本插件进行优化或修复bug，提提issue就好，当然欢迎pr，谢谢了qwq

## 📖 介绍

一个~~就是签到插件的~~赛博女装插件。

## 💿 安装

<details open>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-wearskirt

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-wearskirt
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-wearskirt
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-wearskirt
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-wearskirt
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_wearskirt"]

</details>

## ⚙️ 配置
在 nonebot2 项目的`.env`文件中添加下表中的配置

| 配置项 | 必填 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|
| INTERRUPT_WEAR_SKIRT_TIMES | 否 | false | 不每天连续女装中断女装次数 |

## 🎉 使用
### 指令表
| 指令 | 权限 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| wear_skirt | 任何人 | 否 | 私聊/群聊 | 女装指令 |
| 女装 | 任何人 | 否 | 私聊/群聊 | 女装指令别名 |
