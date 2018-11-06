## 安装自定义glibc
# https://stackoverflow.com/questions/35616650/how-to-upgrade-glibc-from-version-2-12-to-2-14-on-centos
You cannot update glibc on Centos 6 safely. However you can install 2.14 alongside 2.12 easily, then use it to compile projects etc. Here is how:

mkdir ~/glibc_install; cd ~/glibc_install
wget http://ftp.gnu.org/gnu/glibc/glibc-2.14.tar.gz
tar zxvf glibc-2.14.tar.gz
cd glibc-2.14
mkdir build
cd build
../configure --prefix=/opt/glibc-2.14
make -j4
sudo make install
export LD_LIBRARY_PATH=/opt/glibc-2.14/lib


## 查看当前libc版本
ldd --version

## 查看本机支持的glibc版本:
strings /lib64/libc.so.6 |grep GLIBC_
glibc是在 /lib下的libc.so.6中


提示"libc.so.6: version `GLIBC_2.14' not found",原因是系统的glibc版本太低，软件编译时使用了较高版本的glibc引起的：


## 
C++:
    libc 是Linux下的ANSI C函数库
        - libc 实际上是一个泛指。凡是符合实现了 C 标准规定的内容，都是一种 libc 。
    glibc 是Linux下的GUN C函数库
        -   GNU C 函数库是一种类似于第三方插件的东西。
        