Summary: Development Libraries and headers for EFI
Name: gnu-efi
Version: 3.0
Release: 1
Group: Development/System
License: GPL
Source: ftp://ftp.hpl.hp.com/pub/linux-ia64/gnu-efi-%{version}.tar.gz
Patch1: gnu-efi-3.0-makefile.patch
Patch2: gnu-efi-3.0-rodata.patch
BuildRoot: %{_tmppath}/%{name}-%{version}-root
ExclusiveArch: ia64

%description
This package contains development headers and libraries for developing
applications that run under EFI (Extensible Firmware Interface).

%prep
%setup
%patch1 -p1
#%patch2 -p1

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
