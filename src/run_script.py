# -*- coding: utf-8 -*-

import os, sys, subprocess, tempfile, time

TempFile = tempfile.mkdtemp(suffix='_test', prefix='python_')
FileNum = int(time.time()*1000)
EXEC = sys.executable

def get_version():
    v = sys.version_info
    version = "python %s.%s" %(v.major, v.minor)
    return version

def get_pyname():
    global FileNum
    return 'test_%d' % FileNum

def write_file(pyname, code):
    fpath = os.path.join(TempFile, '%s.py' % pyname)
    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(code)
    print('file path: %s' % fpath)
    return fpath

def decode(s):
    try:
        return s.decode('utf-8')
    except UnicodeDecodeError:
        return s.decode('gbk')

def run_main(code):
    r = dict()
    r["version"] = get_version()
    pyname = get_pyname()
    fpath = write_file(pyname, code)
    try:
        outdata = decode(subprocess.check_output([EXEC, fpath], stderr=subprocess.STDOUT, timeout=5))
    except subprocess.CalledProcessError as e:
        r["code"] = 'Error'
        r["output"] = decode(e.output)
        return r
    else:
        r["code"] = "Success"
        r['output'] = outdata
        return r
    finally:
        try:
            os.remove(fpath)
        except Exception as e:
            exit(1)