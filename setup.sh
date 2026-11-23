#!/bin/bash
set -e

echo "1/4: Sistem guncelleniyor..."
sudo apt update && sudo apt upgrade -y

if [ -s "apt-paketleri.txt" ]; then
    echo "2/4: APT paketleri kuruluyor..."
    xargs -a apt-paketleri.txt sudo apt install -y
fi

if [ -s "snap-paketleri.txt" ] && command -v snap >/dev/null 2>&1; then
    echo "3/4: Snap uygulamalari kuruluyor..."
    while read -r pkg; do
        sudo snap install "$pkg" || true
    done < snap-paketleri.txt
fi

if [ -s "python-kutuphaneleri.txt" ]; then
    echo "4/4: Python kutuphaneleri kuruluyor..."
    sudo apt install -y python3-pip
    pip install --user -r python-kutuphaneleri.txt || true
fi

if [ -d "configs" ] && [ "$(ls -A configs)" ]; then
    cp -r configs/. ~/
fi

echo "Tum kurulumlar basariyla tamamlandi!"
