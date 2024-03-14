#!/bin/env bash

# 卸载占用项
sudo apt -y remove --purge brltty

#立即生
sudo chmod 666 /dev/tty*
# 给当前用户添加永久权限，重启生效、
sudo usermod -aG dialout `whoami`
