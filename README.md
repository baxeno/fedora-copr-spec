# fedora-copr-spec

This git repository contains RPM spec files for packages that are not currently in Fedora main repository, but only in my COPR.
My intention is to join the Fedora package maintainer group in Fedora Project.
So I can add them to the main repository as well as maintain some orphan packages I find useful.

**COPR and RPM spec:**

- [Fedora COPR bax/microcom](https://copr.fedorainfracloud.org/coprs/bax/microcom/) needed by Labgrid for embedded Linux device testing.
  - [microcom.spec](microcom.spec)
  - Currently Labgrid installation steps only work for Debian as microcom is required by labgrid-client.
  - So currently it is not very straight forward to also provide Fedora installation steps 🙁

## References

- [Labgrid documentation](https://labgrid.readthedocs.io/en/latest/index.html)
- [Labgrid installation](https://labgrid.readthedocs.io/en/latest/getting_started.html#installation)
- [Labgrid upstream git](https://github.com/labgrid-project/labgrid)
- [Microcom upstream git](https://github.com/pengutronix/microcom)
- [Fedora: Installing Packager Tools](https://docs.fedoraproject.org/en-US/package-maintainers/Installing_Packager_Tools/)
- [Fedora: Joining the Package Maintainers](https://docs.fedoraproject.org/en-US/package-maintainers/Joining_the_Package_Maintainers/)
- [Fedora: Policy for Orphan and Retired Packages](https://docs.fedoraproject.org/en-US/fesco/Policy_for_orphan_and_retired_packages/)
