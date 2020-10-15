# Switchを使えるようにするための環境構築
## インストール方法

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
sudo apt install libudev-dev
sudo apt install libical-dev
sudo apt-get install libudev-dev libical-dev libreadline-dev
sudo pip install bluepy
```
  -  以下のリポジトリをラズパイにインストール.
```sh
git clone https://github.com/OpenWonderLabs/python-host.git
```
  -  ディレクトリ移動
```sh
cd ~/switchbot/python-host
sudo apt install python3-pip
sudo pip3 install pybluez
sudo apt install libboost-python-dev
sudo apt install libboost-thread-dev
sudo pip3 install gattlib
cd
pwd
```
  -  カレントディレクトリが/home/piであることを確認する.
```sh
sudo piip3 download gattlib
ls
```
  -  gattlib-0.20200925.tar.gz(人によって違う).みたいなファイルを見つける
```sh
tar zxvf ./gattlib-0.20200935.tar.gz 
cd ./gattlib-0.20200935.tar.gz
sed -ie 's/boost_python-py34/boost_python-py35/' setup.py
```
  -  シングルコーテーションのところも人によって違うかも
```sh
sudo pip3 install .
sudo apt install libbluetooth3-dev
cd ./switchbot
ls
```
  -  python-hostがあるか確認する
```sh
```
  -  run the python code.
```sh
cd python-host
```

switchボットの使い方はwebを参照

Ubuntu / Debian / Raspbianに必要な依存関係をインストールする方法:

```shell
apt-get install python3-pip
pip3 install pybluez
apt-get install libboost-python-dev
apt-get install libboost-thread-dev
pip3 install gattlib
```

Type `python3 switchbot_py3.py --help` for usage tips.
