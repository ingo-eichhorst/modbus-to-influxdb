# Modbus-to-Influxdb

## Hardware Setup

- Raspberry Pi Zero W
- RS-458 Serial to USB
- USB-Hub with SD-Card slot and FAT32 formatted SD-Card
- Power supply for RaspberryPi and wireing

## Software Setup

- Install influxdb >1.7
- Install and configure grafana >6
- Load grafana dashboard from `grafana.dashboard.json`
- Setup crontab (see Backup below)
- Setup `reader.py` as service in systemd

Or load the image from: `/mnt/image`

## Backup

Backup runs once a day at 4 o'clock AM and saves the data of the previous day to `/mnt/backup/`. See `backup.sh` for details.

Check if cron is running: `tail -n 10000 -f /var/log/syslog | grep CRON`

To restore all backups use:

```bash
  sudo influxd restore -portable -db energy /mnt/backup
```
