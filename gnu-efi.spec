Summary: Development Libraries and headers for EFI
Name: gnu-efi
Version: 3.0a
Release: 5
Group: Development/System
License: GPL
Source: ftp://ftp.hpl.hp.com/pub/linux-ia64/gnu-efi-%{version}.tar.gz
Patch1: gnu-efi-3.0-makefile.patch
Patch2: gnu-efi-3.0-rodata.patch
Patch3: gnu-efi-erikj-reloc.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
ExclusiveArch: ia64

%description
This package contains development headers and libraries for developing
applications that run under EFI (Extensible Firmware Interface).

%prep
%setup
%patch1 -p1
#%patch2 -p1
%patch3 -p0 

%build
make 

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr

make INSTALLROOT=$RPM_BUILD_ROOT/usr install

mkdir -p $RPM_BUILD_ROOT/usr/lib/gnuefi
mv $RPM_BUILD_ROOT/usr/lib/*.lds $RPM_BUILD_ROOT/usr/lib/*.o \
	$RPM_BUILD_ROOT/usr/lib/gnuefi

make -C apps clean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.* ChangeLog apps 
/usr/include/efi
/usr/lib/*

%changelog
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
