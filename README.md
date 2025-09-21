






泰山派上需要cmake3.15及以上版本，可以通过以下步骤安装最新版本的CMake：
```
# 安装编译依赖
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev

# 下载 CMake 最新源码
wget https://cmake.org/files/v3.27/cmake-3.27.9.tar.gz
tar -xvf cmake-3.27.9.tar.gz
cd cmake-3.27.9

# 编译安装
./bootstrap
make -j$(nproc)
sudo make install

# 验证版本
cmake --version
```