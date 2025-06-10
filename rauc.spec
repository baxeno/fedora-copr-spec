Name:           rauc
Version:        1.14
Release:        %autorelease -b 9
Summary:        Safe and secure software updates for embedded Linux

# License issue in de.pengutronix.rauc.Installer.xml
# https://github.com/rauc/rauc/issues/1713
# https://github.com/rauc/rauc/pull/1720
# Upstream: PR is open and expected to be included in release 1.15
License:        LGPL-2.1-only AND CC0-1.0
URL:            https://rauc.io/
Source0:        https://github.com/rauc/%{name}/releases/download/v%{version}/%{name}-%{version}.tar.xz

# Deprecated OpenSSL engine support
# https://github.com/rauc/rauc/issues/1688
# https://github.com/rauc/rauc/pull/1690
# Upstream: PR has landed and will be included in release 1.15
Patch0:         rauc_patch0_no_openssl_engine.patch

# Debian: grub_editenv
# Fedora: grub2_editenv
# Upstream: Work has not yet begun
Patch1:         rauc_patch1_grub_editenv_debian_compat_fix.patch

# 5 tests does not work on F43/Rawhide due to OpenSSL x509 issue
# Tests work on F42 and lower.
# Upstream: Work has not yet begun
Patch2:         rauc_patch2_disable_openssl_x509_issue_on_f43.patch

# RPM lint E: incorrect-fsf-address
# Upstream: Fixed in commit "fe86f27 COPYING: remove old FSF postal address"
#           and will be included in release 1.15
# https://github.com/rauc/rauc/commit/fe86f277258dfe96d0f9ac9bfa930733598d7160

# Exclude architectures that does not have grub2-tools-minimal package
ExcludeArch:    s390 s390x i686

# Tool requirements
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  dbus-devel
BuildRequires:  glib2-devel
BuildRequires:  json-glib-devel
BuildRequires:  libcurl-devel
BuildRequires:  libfdisk-devel
BuildRequires:  libnl3-devel
BuildRequires:  openssl-devel
BuildRequires:  systemd-devel

# Make sure /usr/share/dbus-1/interfaces and /usr/share/dbus-1 are owned.
Requires:  dbus-common
# Weak dependency on documentation
Recommends:  rauc-doc

# Test requirements
BuildRequires:  dbus-daemon
BuildRequires:  e2fsprogs
BuildRequires:  fakeroot
BuildRequires:  grub2-tools-minimal
BuildRequires:  openssl
BuildRequires:  python3-pytest
BuildRequires:  python3-dasbus
BuildRequires:  python3-requests
BuildRequires:  squashfs-tools

%package doc
Summary: RAUC documentation

# rauc-doc does not contain any binaries
BuildArch: noarch

# Documentation requirements
BuildRequires:  make
BuildRequires:  texinfo
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3-sphinx_rtd_theme

%description doc
Documentation for RAUC.

%description
RAUC is a lightweight update client that runs on your Embedded Linux device
and reliably controls the procedure of updating your device with a new firmware
revision. RAUC is also the tool on your host system that lets you create,
inspect and modify update artifacts for your device.
Service is not installed as that is only needed on device.

%prep
%autosetup -v -N
# Fedora deprecated OpenSSL Engine
%patch -P 0 -b .orig
# Debian vs. Fedora grub2 packaging difference
%patch -P 1 -b .orig
# OpenSSL X509 test fails on F43/Rawhide (work on F42 and earlier)
%patch -P 2 -b .orig
# Debian vs. Fedora grub2 packaging difference
cd test/bin
ln -sf grub-editenv grub2-editenv

%build
%meson \
        -Dfuzzing=false \
        -Dhtmldocs=false \
        -Dservice=false \
        -Dstreaming=false \
        -Dnetwork=false

%meson_build

# docbook for yelp or khelpcenter
pushd docs
sphinx-build . texinfo -b texinfo
pushd texinfo
makeinfo --docbook %{name}.texi
popd
popd

%install
%meson_install

# docbook for yelp or khelpcenter
mkdir -p %{buildroot}%{_datadir}/help/en/%{name}
install -m644 docs/texinfo/%{name}.xml %{buildroot}%{_datadir}/help/en/%{name}
cp -p -r docs/texinfo/%{name}-figures %{buildroot}%{_datadir}/help/en/%{name}

%check
%meson_test

%files
%{_bindir}/rauc
%{_datadir}/dbus-1/interfaces/de.pengutronix.rauc.Installer.xml
%license COPYING
%doc README.rst CHANGES
%{_mandir}/man1/rauc.1.*

# docbook for yelp or khelpcenter
%files doc
%dir %{_datadir}/help/en
%doc %lang(en) %{_datadir}/help/en/%{name}

%changelog
* Tue Jun 10 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-9
- Recommend installing separate doc package

* Tue Jun 10 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-8
- Split large documentation into separate doc package

* Wed May 28 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-7
- Change dbus-common dependency from BuildRequires to Requires
- Update upstream license issue and update license information
- Generate docbook for yelp or khelpcenter

* Tue May 20 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-6
- Exclude some architectures that does not have grub2-tools-minimal package
- Add upstream xml file license issue link

* Mon May 19 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-5
- Add dbus-common dependency as xml is installed in dbus-1 directory
- Cleanup patches into 3 logical changes and update upstream status
- Add upstream status of RPM lint incorrect-fsf-address error

* Sat Apr 12 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-4
- Disable 5 tests that does not work on F43/rawhide
- Update files section with macros and add patch comments

* Wed Apr 9 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-3
- Disable network and streaming
- Enable tests and add extra dependencies
- Tests expect Debian host with grub-editenv, called grub2-editenv on Fedora

* Thu Apr 3 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-2
- Add patch that remove OpenSSL engine support

* Wed Apr 2 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.14-1
- Version bumped from 1.13 to 1.14
- Remove test failure comment from spec file

* Thu Mar 13 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.13-1
- Version bumped from 1.11.3 to 1.13

* Mon Feb 10 2025 Bruno Thomsen <bruno.thomsen@gmail.com> - 1.11.3-1
- Initial RPM release with test disabled as 6 fail and 17 ok
