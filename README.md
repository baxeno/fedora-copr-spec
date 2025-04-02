# fedora-copr-spec

This git repository contains RPM spec files for packages that are not currently in Fedora main repository, but only in my COPR.
My intention is to join the Fedora package maintainer group in Fedora Project.
So I can add them to the main repository as well as maintain some orphan packages I find useful.

**COPR and RPM spec:**

- [Fedora COPR bax/microcom](https://copr.fedorainfracloud.org/coprs/bax/microcom/) needed by Labgrid for embedded Linux device testing.
  - [microcom.spec](microcom.spec)
  - Currently Labgrid installation steps only work for Debian as microcom is required by labgrid-client.
  - So currently it is not very straight forward to also provide Fedora installation steps 🙁

- [Fedora COPR bax/rauc](https://copr.fedorainfracloud.org/coprs/bax/rauc/) needed for handling RAUC upgrade bundles for embedded Linux devices.
  - [rauc.spec](rauc.spec)
  - RAUC cli tool can be very useful after an upgrade bundle has been build but not yet released to the wild 🐧
  - resign bundle with new digital signature, e.g. developer signed vs. official signed.
  - inspect bundle meta data or files inside.
  - Service is only needed on target device.
  - Fedora is missing from the list of development/build hosts (Arch, Debian, Ubuntu, NixOS already have package) 🙁

**Test failures if enabling tests for RAUC:**

- Failed to run mksquashfs: Failed to execute child process ?mksquashfs? (No such file or directory) (g-exec-error-quark, 8)
- Failed to spawn child process ?dbus-daemon? (No such file or directory) (g-exec-error-quark, 19)
- Making filesystem failed: Failed to execute child process ?/sbin/mkfs.ext4? (No such file or directory) FAIL
- Transfer failed: Could not resolve host: rauc.io  (g-io-error-quark, 0) FAIL

```
――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――――
22/23 nbd               SKIP             0.01s   0 subtests passed
23/23 boot_switch       SKIP             0.01s   0 subtests passed

Summary of Failures:

 4/23 bundle            ERROR            0.12s   killed by signal 6 SIGABRT
11/23 install           ERROR            0.22s   killed by signal 5 SIGTRAP
14/23 service           ERROR            0.09s   killed by signal 6 SIGABRT
19/23 update_handler    ERROR            0.15s   killed by signal 5 SIGTRAP
21/23 network           ERROR            0.09s   killed by signal 6 SIGABRT

Ok:                 15
Expected Fail:      0
Fail:               5
Unexpected Pass:    0
Skipped:            3
Timeout:            0

%check
%meson_test
```

- [Fedora COPR bax/uuu](https://copr.fedorainfracloud.org/coprs/bax/uuu/) needed for manufacturing of embedded Linux devices with NXP i.MX SoC.
  - [uuu.spec](uuu.spec)
  - UUU (Universal Update Utility), the next evolution of MFGTools, also known as MFGTools v3.
  - Use i.MX USB serial download mode to load Barebox or U-Boot image.
  - Barebox can then expose emmc as mass storage via usb gadget device.

## References

- [Labgrid documentation](https://labgrid.readthedocs.io/en/latest/index.html)
- [Labgrid installation](https://labgrid.readthedocs.io/en/latest/getting_started.html#installation)
- [Labgrid upstream git](https://github.com/labgrid-project/labgrid)
- [Microcom upstream git](https://github.com/pengutronix/microcom)
- [RAUC Safe and Secure OTA Updates for Embedded Linux!](https://rauc.io/)
- [Pengutronix RAUC](https://www.pengutronix.de/en/software/rauc.html)
- [RAUC upstream git](https://github.com/rauc/rauc)
- [UUU upstream git](https://github.com/nxp-imx/mfgtools)
- [Fedora: Installing Packager Tools](https://docs.fedoraproject.org/en-US/package-maintainers/Installing_Packager_Tools/)
- [Fedora: Package Maintenance Guide](https://docs.fedoraproject.org/en-US/package-maintainers/Package_Maintenance_Guide/)
- [Fedora: New Package Process for New Contributors](https://docs.fedoraproject.org/en-US/package-maintainers/New_Package_Process_for_New_Contributors/)
- [Fedora: Joining the Package Maintainers](https://docs.fedoraproject.org/en-US/package-maintainers/Joining_the_Package_Maintainers/)
- [Fedora: Policy for Orphan and Retired Packages](https://docs.fedoraproject.org/en-US/fesco/Policy_for_orphan_and_retired_packages/)
- [Fedora: Fedora Packaging Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/)
- [Fedora: Versioning Guidelines](https://docs.fedoraproject.org/en-US/packaging-guidelines/Versioning/)
- [Fedora: Using the %autorelease Macro](https://docs.pagure.org/fedora-infra.rpmautospec/autorelease.html)
- [Fedora: Copr command line interface](https://developer.fedoraproject.org/deployment/copr/copr-cli.html)
- [RPM %autosetup description](https://rpm-software-management.github.io/rpm/manual/autosetup.html)

