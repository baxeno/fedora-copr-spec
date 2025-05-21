Name:           uuu
Version:        uuu_1.5.201
Release:        %autorelease
Summary:        Universal Update Utility

License:        BSD-3-Clause
URL:            https://github.com/nxp-imx/mfgtools/wiki
Source0:        https://github.com/nxp-imx/mfgtools/releases/download/%{version}/uuu_source-%{version}.tar.gz

# https://github.com/nxp-imx/mfgtools/pull/460
# # Upstream: PR has landed and will be included in next release
Patch0:         uuu_patch0_sdps_gcc15_compile_fix.patch

BuildRequires:  cmake
BuildRequires:  gcc-g++
BuildRequires:  bzip2-devel
BuildRequires:  libusb-compat-0.1-devel
BuildRequires:  libzstd-devel
BuildRequires:  openssl-devel
BuildRequires:  tinyxml2-devel
BuildRequires:  zlib-ng-compat-devel

%description
Universal Update Utility (UUU) is a tool designed for deploying images on NXP
i.MX chips. It is commonly used during manufacturing of devices containing i.MX
based System on Module (SOM). Formerly known as MfgTool (Manufacturing Tool).

%prep
%autosetup -v -N
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
* Wed May 21 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - uuu_1.5.201-1
- Add upstream status for patch
- Expand description

* Sat Mar 15 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - uuu_1.5.182-1
- Add patch that fixes F42 build with GCC15

* Tue Feb 18 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - uuu_1.5.182-1
- Initial RPM release
