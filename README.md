# Serial-Debug

Serial-Debug 是一个基于 PySide6 的串口/网络调试工具，支持串口收发、TCP/UDP 调试、十六进制显示与发送、多条快捷发送、命令补全、数据绘图和在线更新检查。

## 环境要求

- Windows
- Python 3.8+
- 可用串口设备或虚拟串口

## 安装依赖

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## 运行

```powershell
python Serial_Debugger2.py
```

程序运行时会使用 `config/config.json` 保存界面和串口设置，接收数据默认保存到 `data/` 目录。

## 目录结构

```text
.
├── Serial_Debugger2.py      # 主程序入口
├── requirements.txt         # Python 运行依赖
├── assets/                  # 根目录散落的图片/图标资源
├── config/                  # 默认配置、命令补全库和版本信息
├── src/                     # 串口、网络、解析、下载、配置等业务逻辑
├── ui/                      # PySide6 界面代码、Qt Designer 文件和样式
│   ├── design/              # .ui/.qrc 原始设计资源
│   └── resources/           # pyside6-rcc 生成的 Qt 资源模块
└── data/                    # 运行时数据目录，已被 .gitignore 忽略
```

## UI 和资源文件

`ui/design/` 下保留 Qt Designer 的 `.ui` 与 `.qrc` 源文件。修改界面或图标资源后，可重新生成对应 Python 文件：

```powershell
pyside6-uic ui\design\Serial_MainWindow.ui -o ui\Serial_MainWindow_ui.py
pyside6-rcc ui\design\icoPack.qrc -o ui\resources\icoPack_rc.py
pyside6-rcc ui\design\cmdSetWindow.qrc -o ui\resources\cmdSetWindow_rc.py
```

生成后的资源模块通过 `from ui.resources import icoPack_rc` 和 `from ui.resources import cmdSetWindow_rc` 导入。

## 维护说明

- `config/CMDList.json` 是命令补全数据源，可在程序内通过命令集管理窗口修改。
- `config/versionInfo.json` 用于在线更新检查的本地版本信息。
- `src/app_paths.py` 统一维护项目路径，新增配置或运行时文件时优先放在这里。
- `__pycache__`、`build/`、`dist/`、`data/`、`download/` 等运行或打包产物不应提交到仓库。

## Git 远端

当前仓库关联到：

```text
https://github.com/Unarvest/Serial-Debug.git
```

如果没有原仓库写权限，请先 fork，再把 `origin` 改成自己的 fork 地址后提交。
