# VMware Ubuntu Geliştirme Ortamı (ROS Noetic & Gazebo)

Bu depo, VMware üzerinde çalışan Ubuntu 20.04 (Focal) sanal makinesinin kurulum adımlarını, yüklü sistem/ROS/Python paket listelerini ve yapılandırma ayarlarını içerir.

## 1. VMware Sanal Makine Ayarları
- **İşletim Sistemi:** Ubuntu 20.04 Desktop (64-bit)
- **Önerilen RAM:** En az 4 GB (Gazebo simülasyonları için 8 GB önerilir)
- **İşlemci:** 2 veya 4 Çekirdek
- **Disk Alanı:** En az 30 GB
- **Ağ Bağdaştırıcısı:** NAT

## 2. Sıfırdan Kurulum Adımları
1. Ubuntu kurulumunu tamamladıktan sonra terminali açın (`Ctrl + Alt + T`).
2. Ekran çözünürlüğü, kopyala-yapıştır desteği ve Git için gerekli araçları kurun:

       sudo apt update && sudo apt install -y open-vm-tools-desktop git

3. Bu depoyu bilgisayarınıza indirin ve otomatik kurulumu başlatın:

       git clone https://github.com/EBurak03/ubuntu-vm-rehberi.git
       cd ubuntu-vm-rehberi
       ./setup.sh

## 3. Yüklü Ana Bileşenler
- **Robotik & Simülasyon:** ROS Noetic Desktop Full, Gazebo 11, TurtleBot3 paketleri
- **Gömülü Sistem & Derleyiciler:** `gcc-arm-none-eabi`, `esptool`, `cmake`, `gdb-multiarch`, `clang`
- **Editör & Araçlar:** Visual Studio Code (Snap), Mono, OpenCV, Eigen3
