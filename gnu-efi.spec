Summary: Development Libraries and headers for EFI
Name: gnu-efi
Version: 3.0e
Release: 1%{?dist}
Group: Development/System
License: GPLv2+
URL: ftp://ftp.hpl.hp.com/pub/linux-ia64
Source: ftp://ftp.hpl.hp.com/pub/linux-ia64/gnu-efi-%{version}.tar.bz2
Patch0: gnu-efi-3.0e-no-relocations.patch
Patch1: gnu-efi-3.0d-unwrap.patch
Patch2: gnu-efi-3.0d-uefi_wrap.patch
Patch3: gnu-efi-3.0d-uefi_wrap_call10.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch: i386 x86_64

%description
This package contains development headers and libraries for developing
applications that run under EFI (Extensible Firmware Interface).

%prep
%setup -q
%patch0 -p1
# these are currently disabled as we don't need them per se, and they
# haven't gone upstream yet either.  Also #2 and #3 haven't been updated
# to work with gnu-efi-3.0e yet.
#%%patch1 -p1
#%%patch2 -p1
#%%patch3 -p1

%build
# Package cannot build with %{?_smp_mflags}.
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_libdir}

make INSTALLROOT=%{buildroot}/%{_prefix} install

mkdir -p %{buildroot}/%{_libdir}/gnuefi
mv %{buildroot}/%{_libdir}/*.lds %{buildroot}/%{_libdir}/*.o %{buildroot}/%{_libdir}/gnuefi

make -C apps clean

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.* ChangeLog apps
%{_includedir}/efi
%{_libdir}/*

%changelog
* Thu Oct 02 2008 Peter Jones <pjones@redhat.com> - 3.0e-1
- Update to 3.0e
- Fix relocation bug in 3.0e

* Tue Jul 29 2008 Tom "spot" Callaway <tcallawa@redhat.com> - 3.0d-6
- fix license tag

* Mon Jul 28 2008 Peter Jones <pjones@redhat.com> - 3.0d-5
- Remove ia64 palproc code since its license isn't usable.
- Remove ia64 from ExclusiveArch since it can't build...

* Thu Mar 27 2008 Peter Jones <pjones@redhat.com> - 3.0d-4
- Fix uefi_call_wrapper(x, 10, ...) .
- Add efi_main wrappers and EFI_CALL() macro so drivers are possible.

* Mon Feb 18 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 3.0d-3
- Autorebuild for GCC 4.3

* Fri Jan 11 2008 Peter Jones <pjones@redhat.com> - 3.0d-2
- Get rid of a bogus #ifdef .

* Wed Dec 19 2007 Peter Jones <pjones@redhat.com> - 3.0d-1
- Update to 3.0d

* Tue Jun 12 2007 Chris Lumens <clumens@redhat.com> - 3.0c-2
- Fixes for package review (#225846).

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 3.0c-1.1
- rebuild

* Thu Apr 27 2006 Chris Lumens <clumens@redhat.com> 3.0c-1
- Upgrade to gnu-efi-3.0c.
- Enable build on i386.

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 3.0a-7.2
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Thu Mar  3 2005 Jeremy Katz <katzj@redhat.com> - 3.0a-7
- rebuild with gcc 4

* Tue Sep 21 2004 Jeremy Katz <katzj@redhat.com> - 3.0a-6
- add fix from Jesse Barnes for newer binutils (#129197)

* Tue Jun 15 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Wed Apr 21 2004 Jeremy Katz <katzj@redhat.com> - 3.0a-4
- actually add the patch

* Tue Apr 20 2004 Bill Nottingham <notting@redhat.com> 3.0a-3
- add patch to coalesce some relocations (#120080, <erikj@sgi.com>)

* Fri Feb 13 2004 Elliot Lee <sopwith@redhat.com>
- rebuilt

* Fri Oct  4 2002 Jeremy Katz <katzj@redhat.com>
- rebuild in new environment

* Sun Jul  8 2001 Bill Nottingham <notting@redhat.com>
- update to 3.0

* Tue Jun  5 2001 Bill Nottingham <notting@redhat.com>
- add fix for invocations from the boot manager menu (#42222)

* Tue May 22 2001 Bill Nottingham <notting@redhat.com>
- add bugfix for efibootmgr (<schwab@suse.de>)

* Mon May 21 2001 Bill Nottingham <notting@redhat.com>
- update to 2.5
- add in efibootmgr from Dell (<Matt_Domsch@dell.com>)

* Thu May  3 2001 Bill Nottingham <notting@redhat.com>
- fix booting of kernels with extra arguments (#37711)

* Wed Apr 25 2001 Bill Nottingham <notting@redhat.com>
- take out Stephane's initrd patch

* Fri Apr 20 2001 Bill Nottingham <notting@redhat.com>
- fix the verbosity patch to not break passing arguments to images

* Wed Apr 18 2001 Bill Nottingham <notting@redhat.com>
- update to 2.0, build elilo, obsolete eli

* Tue Dec  5 2000 Bill Nottingham <notting@redhat.com>
- update to 1.1

* Thu Oct 26 2000 Bill Nottingham <notting@redhat.com>
- add patch for new toolchain, update to 1.0

* Thu Aug 17 2000 Bill Nottingham <notting@redhat.com>
- update to 0.9
