Name:           microcom
Version:        2023.09.0
Release:        1%{?dist}
Summary:        minimalistic terminal program

License:        GPL-2.0-only
URL:            https://github.com/pengutronix/%{name}
Source0:        https://github.com/pengutronix/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  readline-devel, gcc

%description
microcom is a minimalistic terminal program for accessing devices (e.g.
switches) via a serial connection.  It features connection via RS232
serial interfaces (including setting of transferrates) as well as in
"telnet mode" as specified in rfc2217.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
/usr/bin/microcom
%license COPYING
%doc README.md
/usr/share/man/man1/microcom.1.gz

%changelog
* Wed Jun 05 2024 Bruno Thomsen <bruno.thomsen@gmail.com>
- Initial RPM release
