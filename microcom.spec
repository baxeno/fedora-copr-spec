Name:           microcom
Version:        2023.09.0
Release:        %autorelease
Summary:        minimalistic terminal program

# Upstream status: work not started
# incorrect-fsf-address in COPYING
License:        GPL-2.0-only
URL:            https://github.com/pengutronix/%{name}
Source0:        https://github.com/pengutronix/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  readline-devel

%description
Microcom is a minimalistic terminal program for accessing devices (e.g.
switches) via a serial connection.  It features connection via RS232
serial interfaces (including setting of transfer-rates) as well as in
"telnet mode" as specified in rfc2217.

%prep
%autosetup

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/microcom
%license COPYING
%doc README.md
%{_mandir}/man1/microcom.1.*

%changelog
* Wed May 21 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 2023.09.0-1
- Use macros in files section
- Minor spec file cleanup

* Wed Jun 05 2024 Bruno Thomsen <bruno.thomsen@gmail.com> - 2023.09.0-1
- Initial RPM release
