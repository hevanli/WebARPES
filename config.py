import os
from pathlib import Path

basedir = Path(__file__).absolute() / "uploads"
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'temp-secret-key'
    BOOTSTRAP_BTN_STYLE = 'primary'