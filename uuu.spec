Name:           uuu
Version:        uuu_1.5.182
Release:        %autorelease
Summary:        Universal Update Utility

License:        BSD-3-Clause
URL:            https://github.com/nxp-imx/mfgtools/wiki
Source0:        https://github.com/nxp-imx/mfgtools/releases/download/%{version}/uuu_source-%{version}.tar.gz
Patch0:         sdps_gcc15_compile_fix.patch

BuildRequires:  cmake
BuildRequires:  gcc-g++
BuildRequires:  openssl-devel
BuildRequires:  bzip2-devel
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  libzstd-devel
BuildRequires:  zlib-ng-compat-devel
BuildRequires:  tinyxml2-devel

%description
Universal Update Utility (UUU) is a tool designed for deploying images on NXP i.MX chips.

%prep
%autosetup -v -N
cd libuuu
%patch -P 0 -b .orig

%build
%cmake -Dstatic=OFF -DCMAKE_BUILD_TYPE=RELEASE
%cmake_build

%install
%cmake_install

%files
/usr/bin/uuu
%license LICENSE
%doc README.md

%changelog
* Sat Mar 15 2025 Bruno Thomsen <bruno.thomsen@gmail.com>
- add sdps_gcc15_compile_fix.patch that fixes F42 build with GCC15
* Tue Feb 18 2025 Bruno Thomsen <bruno.thomsen@gmail.com>
- Initial RPM release
