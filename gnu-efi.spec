Summary: Development Libraries and headers for EFI
Name: gnu-efi
Version: 3.0e
Release: 16%{?dist}
Group: Development/System
License: GPLv2+
URL: ftp://ftp.hpl.hp.com/pub/linux-ia64
Source: ftp://ftp.hpl.hp.com/pub/linux-ia64/gnu-efi-%{version}.tar.bz2
Patch0: gnu-efi-3.0e-no-relocations.patch
Patch1: gnu-efi-3.0e-Fix-usage-of-INSTALLROOT-PREFIX-and-LIBDIR.patch
Patch2: gnu-efi-3.0e-ignore-gnu-stack.patch
Patch3: gnu-efi-3.0e-add-uefi-2.x-boot-services.patch
Patch4: gnu-efi-3.0e-add-pciio.patch
Patch5: gnu-efi-3.0e-route80h.patch
Patch6: gnu-efi-3.0e-modelist.patch
Patch7: gnu-efi-3.0e-route80h-add-cougarpoint.patch
Patch8: gnu-efi-3.0e-machine-types.patch
Patch9: gnu-efi-3.0e-handle-uninitialized-gop.patch
Patch10: gnu-efi-3.0e-Add-.S-and-.E-rules.patch
Patch11: gnu-efi-3.0e-Guarantee-16-byte-stack-alignment-on-x86_64-efi_call.patch
Patch12: gnu-efi-3.0e-Add-the-routines-to-make-callbacks-work.patch
Patch13: gnu-efi-3.0e-Add-tcc.efi-to-test-our-calling-convention-shananaga.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
ExclusiveArch: i686 x86_64 ia64
BuildRequires: git

%define debug_package %{nil}

%description
This package contains development headers and libraries for developing
applications that run under EFI (Extensible Firmware Interface).

%prep
%setup -q
git init
git config user.email "pjones@fedoraproject.org"
git config user.name "Fedora Ninjas"
git add .
git commit -a -q -m "%{version} baseline."
git am %{patches}

%build
# Package cannot build with %{?_smp_mflags}.
make

%install
rm -rf %{buildroot}

mkdir -p %{buildroot}/%{_libdir}

make PREFIX=%{_prefix} LIBDIR=%{_libdir} INSTALLROOT=%{buildroot} install

mkdir -p %{buildroot}/%{_libdir}/gnuefi
mv %{buildroot}/%{_libdir}/*.lds %{buildroot}/%{_libdir}/*.o %{buildroot}/%{_libdir}/gnuefi

make -C apps clean route80h.efi modelist.efi
mkdir -p %{buildroot}/boot/efi/EFI/redhat/
mv apps/{route80h.efi,modelist.efi} %{buildroot}/boot/efi/EFI/redhat/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README.* ChangeLog
%{_includedir}/efi
%{_libdir}/*
%dir /boot/efi/EFI/redhat/
%attr(0644,root,root) /boot/efi/EFI/redhat/*.efi

%changelog
* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0e-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Aug 11 2011 Peter Jones <pjones@redhat.com> - 3.0e-15
- Correctly pad the stack when doing uefi calls
  Related: rhbz#677468
- Add ability to write UEFI callbacks and drivers
- Add test harness for ABI Calling Conventions

* Thu Jun 16 2011 Peter Jones <pjones@redhat.com> - 3.0e-14
- Handle uninitialized GOP driver gracefully.

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0e-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Sep 10 2010 Peter Jones <pjones@redhat.com> - 3.0e-12
- Add "modelist.efi" test utility in apps/

* Mon Jul 26 2010 Peter Jones <pjones@redhat.com> - 3.0e-11
- Add PciIo headers.

* Fri Jul 23 2010 Peter Jones <pjones@redhat.com> - 3.0e-10
- Add UEFI 2.x boot services.

* Tue Aug 11 2009 Peter Jones <pjones@redhat.com> - 3.0e-9
- Change ExclusiveArch to reflect arch changes in repos.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0e-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Fri Apr 03 2009 Peter Jones <pjones@redhat.com> - 3.0e-7
- Use nickc's workaround for #492183

* Tue Mar 31 2009 Peter Jones <pjones@redhat.com> - 3.0e-6.1
- Make a test package for nickc.

* Thu Mar 12 2009 Chris Lumens <clumens@redhat.com> 3.0e-6
- Add IA64 back into the list of build arches (#489544).

* Mon Mar 02 2009 Peter Jones <pjones@redhat.com> - 3.0e-5
- Switch to i586 from i386.

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 3.0e-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Fri Feb 13 2009 Peter Jones <pjones@redhat.com> - 3.0e-3
- Pad sections out in the provided linker scripts to make sure they all of
  some content.

* Fri Oct 03 2008 Peter Jones <pjones@redhat.com> - 3.0e-2
- Fix install paths on x86_64.

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
