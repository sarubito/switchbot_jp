# python-host

# What is the SwitchBot opensource project?
[SwitchBot](https://www.switch-bot.com) is a smart IoT robot to mechanically control all your switches and buttons. You can control the bot by your smartphone app ([iOS](https://itunes.apple.com/app/SwitchBot/id1087374760?mt=8) or  [Android](https://play.google.com/store/apps/details?id=com.theSwitchBot.SwitchBot), SwitchLink, or other platform based on our open APIs.

This project aims to provide a super light-weight solution to control your SwitchBot on [Raspberry Pi](https://www.raspberrypi.org)/[OpenWRT](https://openwrt.org/) or any other Linux based board.

The python-host distribution is supported and tested on Python 2.7.

# インストール方法

用意するもの:
  -  raspberry pi2かraspberry pi3のどちらかを用意(pi3に関してはデフォルトでBluetoothがある)
  -  Switchbot
  -  An SD Card with a fresh install of Raspbian

インストール:新規インストールされているRaspbian.
  -  必要なライブラリをインストール.
```sh
sudo apt-get update
sudo apt-get install python-pexpect
sudo apt-get install libusb-dev libdbus-1-dev libglib2.0-dev 
sudo apt-get install libudev-dev libical-dev libreadline-dev
sudo pip install bluepy
```
  -  以下のリポジトリをラズパイにインストール.
```sh
git clone https://github.com/OpenWonderLabs/python-host.git
```
  -  run the python code.
```sh
cd python-host
```
You can use in two ways:

1. Scan and control by device name.
```
sudo python switchbot.py
```
  -  Follow the instruction, input the device number for SwitchBot you want to control.

2. Control SwitchBot by MAC address. (MAC address should be retrived in advanced)
```
sudo python switchbot.py [mac_addr action_cmd]
```
action_cmd :Press, Turn On, Turn Off.
```
eg: sudo python switchbot.py  xx:xx:xx:xx:xx:xx Press
```

3. Python 3 and new bluetooth stack support

The original `switchbot.py` script will work only on Python 2 and it relies on the old Bluez utils (like `hciconfig` and `hcitool`) that have been deprecated in the latest Bluez releases.

If you want to use the script on Python 3 or on a Linux distro that no longer ships Bluez with the old tools, use the switchbot_py3.py script instead.

To install the required dependencies on Ubuntu/Debian/Raspbian:

```shell
apt-get install python3-pip
pip3 install pybluez
apt-get install libboost-python-dev
apt-get install libboost-thread-dev
pip3 install gattlib
```

If for some reason the gattlib installation fails:

```shell
pip3 download gattlib
tar xvzf ./gattlib-0.20150805.tar.gz
cd gattlib-0.20150805/
sed -ie 's/boost_python-py34/boost_python-py35/' setup.py
pip3 install .
```
gattlibのインストールでも苦戦する場合

Type `python3 switchbot_py3.py --help` for usage tips.

Enjoy :)

# Thanks to contributors:
BlackLight

Share your words in our [community](http://www.switch-bot.com/forum).
