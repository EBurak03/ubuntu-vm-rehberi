#!/bin/bash
set -e

echo "1/5: Harici depo kaynaklari (ROS, Gazebo, Mono) ekleniyor..."
if [ -d "configs/apt-keys" ] && [ "$(ls -A configs/apt-keys)" ]; then
    sudo cp -r configs/apt-keys/. /etc/apt/trusted.gpg.d/
fi
if [ -d "configs/apt-sources" ] && [ "$(ls -A configs/apt-sources)" ]; then
    sudo cp -r configs/apt-sources/. /etc/apt/sources.list.d/
fi

echo "2/5: Sistem guncelleniyor..."
sudo apt update && sudo apt upgrade -y

if [ -s "apt-paketleri.txt" ]; then
    echo "3/5: APT paketleri kuruluyor..."
    xargs -a apt-paketleri.txt sudo apt install -y
fi

if [ -s "snap-paketleri.txt" ] && command -v snap >/dev/null 2>&1; then
    echo "4/5: Snap uygulamalari kuruluyor..."
    while read -r pkg; do
        sudo snap install "$pkg" || true
    done < snap-paketleri.txt
fi

if [ -s "python-kutuphaneleri.txt" ]; then
    echo "5/5: Python kutuphaneleri kuruluyor..."
    sudo apt install -y python3-pip
    pip install --user -r python-kutuphaneleri.txt || true
fi

cp -f configs/.bashrc ~/ 2>/dev/null || true
cp -f configs/.profile ~/ 2>/dev/null || true

echo "Tum kurulumlar basariyla tamamlandi!"
