Summary: Development Libraries and headers for EFI
Name: gnu-efi
Version: 2.5
Release: 3
Group: Development/System
License: GPL
Source: ftp://ftp.hpl.hp.com/pub/linux-ia64/gnu-efi-%{version}.tar.gz
Patch: gnu-efi-2.5-makefile.patch
Patch2: efibootmgr-0.3.1-remove-from-bootorder.patch
Patch3: elilo-2.5-prompt.patch
Source1: http://domsch.com/linux/ia64/efibootmgr-0.3.1.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-root
ExclusiveArch: ia64

%description
This package contains development headers and libraries for developing
applications that run under EFI (Extensible Firmware Interface).

%package -n elilo
Summary: ELILO linux boot loader for EFI-based systems
Group: System Environment/Base
Obsoletes: eli

%description -n elilo
ELILO is a linux boot loader for EFI-based systems, such as IA-64.

%prep
%setup -a 1
%patch -p1 
%patch2 -p0
%patch3 -p0

%build
make CFLAGS="$RPM_OPT_FLAGS"
cd efibootmgr-0.3.1
make
cp COPYING INSTALL README doc
mv doc efibootmgr-doc
cd ..

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT/usr/{bin,include/efi,lib/gnuefi}

for header in inc/*.h ; do
	install -m 644 $header $RPM_BUILD_ROOT/usr/include/efi
done

make -C apps clean

mkdir -p $RPM_BUILD_ROOT/usr/include/efi/%{_arch}
install -m 644 inc/%{_arch}/*.h $RPM_BUILD_ROOT/usr/include/efi/%{_arch}

install -m644 gnuefi/libgnuefi.a $RPM_BUILD_ROOT/usr/lib
install -m644 lib/libefi.a $RPM_BUILD_ROOT/usr/lib

install -m644 gnuefi/crt0-efi-%{_arch}.o $RPM_BUILD_ROOT/usr/lib/gnuefi
install -m644 gnuefi/elf_%{_arch}_efi.lds $RPM_BUILD_ROOT/usr/lib/gnuefi

mkdir -p $RPM_BUILD_ROOT/boot/efi/efi/boot
install -m 755 elilo/elilo.efi $RPM_BUILD_ROOT/boot/efi/elilo.efi
install -m 755 elilo/elilo.efi $RPM_BUILD_ROOT/boot/efi/efi/boot/bootia64.efi

mkdir -p $RPM_BUILD_ROOT/usr/sbin
install -m 755 efibootmgr-0.3.1/src/efibootmgr/efibootmgr $RPM_BUILD_ROOT/usr/sbin

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README README.efilib ChangeLog apps 
/usr/include/efi
/usr/lib/*

%files -n elilo
%defattr(-,root,root)
%doc elilo/README elilo/TODO elilo/elilo.txt efibootmgr-0.3.1/efibootmgr-doc 
/boot/efi/elilo.efi
/boot/efi/efi/boot/bootia64.efi
/usr/sbin/efibootmgr

%changelog
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
