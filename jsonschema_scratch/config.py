import os


APP_ABS_DIR = os.getcwd()

SCHEMAS_DIR_NAME = "schemas"
SCHEMAS_ABS_DIR = os.path.join(APP_ABS_DIR, SCHEMAS_DIR_NAME)
SCHEMAS_BASE_URI = "file:///{}/".format(SCHEMAS_ABS_DIR)
SCHEMAS_RELATIVE_PATH = "../schemas"
