Name:           rauc
Version:        1.14
Release:        %autorelease
Summary:        Safe and secure software updates for embedded Linux

License:        LGPL-2.1-only
URL:            https://rauc.io/
Source0:        https://github.com/rauc/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz
Patch0:         rauc_no_openssl_engine.patch
Patch1:         rauc_bootloader_grub_editenv.patch
Patch2:         rauc_grub_editenv.patch

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  dbus-devel
BuildRequires:  openssl-devel
BuildRequires:  libcurl-devel
BuildRequires:  libfdisk-devel
BuildRequires:  libnl3-devel
BuildRequires:  systemd-devel

# Test requirements
BuildRequires:  e2fsprogs
BuildRequires:  squashfs-tools
BuildRequires:  dbus-daemon
BuildRequires:  fakeroot
BuildRequires:  python3-pytest
BuildRequires:  python3-dasbus
BuildRequires:  python3-requests
BuildRequires:  grub2-tools-minimal
BuildRequires:  openssl

%description
RAUC is a lightweight update client that runs on your Embedded Linux device
and reliably controls the procedure of updating your device with a new firmware
revision. RAUC is also the tool on your host system that lets you create,
inspect and modify update artifacts for your device.
Service is not installed as that is only needed on device.

%prep
%autosetup -v -N
cd src
%patch -P 0 -b .orig
cd bootloaders
%patch -P 1 -b .orig
cd ../../test
%patch -P 2 -b .orig
cd bin
ln -sf grub-editenv grub2-editenv

%build
%meson \
        -Dfuzzing=false \
        -Dhtmldocs=false \
        -Dservice=false \
        -Dstreaming=false \
        -Dnetwork=false

%meson_build

%install
%meson_install

%check
%meson_test

%files
/usr/bin/rauc
/usr/share/dbus-1/interfaces/de.pengutronix.rauc.Installer.xml
%license COPYING
%doc README.rst
/usr/share/man/man1/rauc.1.gz

%changelog
* Wed Apr 9 2025 Bruno Thomsen <bruno.thomsen@gmail.com>
- Disable network and streaming
- Enable tests and add extra dependencies
- Tests expect Debian host with grub-editenv, called grub2-editenv on Fedora.

* Thu Apr 3 2025 Bruno Thomsen <bruno.thomsen@gmail.com>
- Add patch that remove OpenSSL engine support

* Wed Apr 2 2025 Bruno Thomsen <bruno.thomsen@gmail.com>
- Version bumped from 1.13 to 1.14
- Remove test failure comment from spec file

* Thu Mar 13 2025 Bruno Thomsen <bruno.thomsen@gmail.com>
- Version bumped from 1.11.3 to 1.13

* Mon Feb 10 2025 Bruno Thomsen <bruno.thomsen@gmail.com>
- Initial RPM release with test disabled as 6 fail and 17 ok
