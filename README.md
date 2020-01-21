
# Members

Obdoba: 
https://github.com/jitka/tajemstvi

## Run

Build image: `docker build -t members .`

Ve Fedoře je ještě třeba vypnout selinux: `sudo /sbin/setenforce 0`,
v Ubuntu/debianu můžete pouštět docker pod rootem nebo zkusit podman 
(TODO otestovat)

Run image: `docker run --name members -v "$PWD/instance:/app/instance:rw" -p 80:80 --rm members`

