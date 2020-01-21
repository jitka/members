
# Members

Obdoba: 
https://github.com/jitka/tajemstvi

## Ruční spuštění
```
cd app
python3 -m venv env
. env/bin/activate
pip3 install -r requirements.txt
python3 ./main.py
```


## Docker
(poznámka neotestováno

Build image: `docker build -t members .`

Ve Fedoře je ještě třeba vypnout selinux: `sudo /sbin/setenforce 0`,
v Ubuntu/debianu můžete pouštět docker pod rootem nebo zkusit podman 
(TODO otestovat)

Run image: `docker run --name members -v "$PWD/instance:/app/instance:rw" -p 80:80 --rm members`

