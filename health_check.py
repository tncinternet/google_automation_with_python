#!/usr/bin/env python3

import psutil
import shutil
import socket
import emails


cpu_usage = psutil.cpu_percent(1)
print(cpu_usage)

disk = psutil.disk_usage('/')
free_disk = disk.free/disk.total * 100
print(free_disk)

mem_threshold = 500 * 1024 * 1024
memory_available = psutil.virtual_memory()._asdict()['available']
print(memory_available)

target_host = '127.0.0.1'
hostname = socket.gethostbyname('localhost')
print(hostname)

cond_1 = cpu_usage > 80
cond_2 = free_disk < 20
cond_3 = memory_available < mem_threshold
cond_4 = hostname != target_host

conditions = cond_1 | cond_2 | cond_3 | cond_4

if conditions:
    sender = "automation@example.com"
    recipient = "@example.com"
    body = "Please check your system and resolve the issue as soon as possible."
    subject = ""
    if cond_1:
        subject = "ERROR - CPU usage is over 80%,"
    if cond_2:
        subject = "ERROR - Available disk space is less than 20%,"
    if cond_3:
        subject = "ERROR - Available memory is less than 500MB,"
    if cond_4:
        subject = "ERROR - localhost cannot be resolved to 127.0.0.1,"

    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)
