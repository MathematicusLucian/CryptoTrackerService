# -*- coding: utf-8 -*-
import pkgutil
import importlib
from flask import Blueprint
# from pathlib import Path
import os
from dotenv import load_dotenv

# return rv (list): list of blueprints
def register_blueprints(app, package_name, package_path):
    blue_prints = []
    for _, name, _ in pkgutil.iter_modules(package_path):
        files = importlib.import_module('%s.%s' % (package_name, name))
        for item in dir(files):
            item = getattr(files, item)
            if isinstance(item, Blueprint):
                app.register_blueprint(item)
            blue_prints.append(item)
    return blue_prints

def get_config(envar_key):
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.join(BASEDIR, '.env'))
    return os.getenv(envar_key)