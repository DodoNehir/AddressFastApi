import subprocess as sp

PORT = 8080
RELOAD = True

cmd = [
  'uvicorn', 'app:app'
]

if PORT :
    cmd += ['--host', '0.0.0.0', '--port', format(PORT)]

if RELOAD :
    cmd.append('--reload')

sp.run(cmd)