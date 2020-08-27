#!/bin/bash
# License of this script: CC0
# Installation of dependent libraries and softwares is required to use this script
# ex. nasm, yasm, libmp3lame-dev, libopus-dev, libvorbis-dev, libvpx-dev...

apt-get install -y libopus-dev

set -ex

# setup
temp_dir=$(mktemp -d)

# build openh264
cd $temp_dir
git clone -b v1.7.0 --depth 1 --single-branch https://github.com/cisco/openh264.git
cd openh264
make -j `nproc`
make install
ldconfig

# replace openh264 binary to avoid license problem
cd $temp_dir
curl -o ./libopenh264-1.7.0-linux64.4.so.bz2 -L https://github.com/cisco/openh264/releases/download/v1.7.0/libopenh264-1.7.0-linux64.4.so.bz2
bunzip2 libopenh264-1.7.0-linux64.4.so.bz2
cp libopenh264-1.7.0-linux64.4.so /usr/local/lib/libopenh264.so.1.7.0
rm /usr/local/lib/libopenh264.a

# build ffmpeg
cd $temp_dir
git clone https://git.ffmpeg.org/ffmpeg.git
cd ffmpeg
git checkout n3.4.2
# export PKG_CONFIG_PATH=/usr/local/lib/pkgconfig
# ./configure --enable-libopenh264 --enable-libmp3lame --enable-libopus --enable-libvorbis --enable-libvpx
# make -j `nproc`
# make install

# cleanup
cd
rm -rf $temp_dir
