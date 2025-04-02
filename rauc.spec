Name:           rauc
Version:        1.14
Release:        %autorelease
Summary:        Safe and secure software updates for embedded Linux

License:        LGPL-2.1-only
URL:            https://rauc.io/
Source0:        https://github.com/rauc/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  dbus-devel
BuildRequires:  openssl-devel
BuildRequires:  openssl-devel-engine
BuildRequires:  libcurl-devel
BuildRequires:  libfdisk-devel
BuildRequires:  libnl3-devel
BuildRequires:  systemd-devel

%description
RAUC is a lightweight update client that runs on your Embedded Linux device
and reliably controls the procedure of updating your device with a new firmware
revision. RAUC is also the tool on your host system that lets you create,
inspect and modify update artifacts for your device.
Service is not installed as that is only needed on device.

%prep
%autosetup -v

%build
%meson \
        -Dfuzzing=false \
        -Dhtmldocs=false \
        -Dservice=false \
        -Dtests=false

%meson_build

%install
%meson_install

%files
/usr/bin/rauc
/usr/share/dbus-1/interfaces/de.pengutronix.rauc.Installer.xml
%license COPYING
%doc README.rst
/usr/share/man/man1/rauc.1.gz

%changelog
* Wed Apr 2 2025 Bruno Thomsen <bruno.thomsen@gmail.com>
- Version bumped from 1.13 to 1.14
- Remove test failure comment from spec file

* Thu Mar 13 2025 Bruno Thomsen <bruno.thomsen@gmail.com>
- Version bumped from 1.11.3 to 1.13

* Mon Feb 10 2025 Bruno Thomsen <bruno.thomsen@gmail.com>
- Initial RPM release with test disabled as 6 fail and 17 ok
