from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = PROJECT_ROOT / "config"
DATA_DIR = PROJECT_ROOT / "data"
CONFIG_FILE = CONFIG_DIR / "config.json"
CMD_LIST_FILE = CONFIG_DIR / "CMDList.json"
VERSION_INFO_FILE = CONFIG_DIR / "versionInfo.json"
DOWNLOAD_DIR = PROJECT_ROOT / "download"
