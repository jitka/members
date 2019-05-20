
# Tajemstvi

Obdoba: https://github.com/Kedrigern/docker/tree/master/flask3-cislovky

## Run

Build image: `docker build -t tajemstvi .`

Ve Fedoře je ještě třeba vypnout selinux: `sudo /sbin/setenforce 0`

Run image: `docker run --name tajemstvi -v "$PWD/instance:/app/instance:rw" -p 80:80 --rm tajemstvi`

## DB

Využije se: `instance/tajemstvi.sqlite` (a je tedy i perzistentní)

Pokud chceme vynulovat počítadlo, tak prázdná inicializovaná DB: `instance/tajemstvi-empty.sql`