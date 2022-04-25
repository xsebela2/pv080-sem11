# contains bunch of buggy examples
# taken from https://hackernoon.com/10-common-security-gotchas-in-python-and-how-to-avoid-them-e19fbe265e03
import base64
import pickle
import subprocess
import flask

# Input injection
from flask import app


def transcode_file(request, filename):
    sanitized = filename.replace("\"", "\\\"")
    command = f'ffmpeg -i {sanitized} output_file.mpg'
    subprocess.call(command, shell=True)  # a bad idea!


# Assert statements
def foo(request, user):
    if not user.is_admin:
        raise PermissionError("user does not have access")
    request(user)
    # secure code...


# Pickles
class RunBinSh:
    def __reduce__(self):
        return (subprocess.Popen, (('/bin/sh',),))

def import_urlib_version(version):
    exec(f"import urllib{version} as urllib")

@app.route('/')
def index():
    module = flask.request.args.get("module")
    import_urlib_version(module)


print(base64.b64encode(pickle.dumps(RunBinSh())))
