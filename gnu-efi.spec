Summary: Development Libraries and headers for EFI
Name: gnu-efi
Version: 1.1
Release: 1
Group: Development/System
License: GPL
Source: ftp://ftp.hpl.hp.com/pub/linux-ia64/gnu-efi-%{version}.tgz
Patch: gnu-efi-1.1-build.patch
Patch2: gnu-efi-1.1-netshut.patch
BuildRoot: /var/tmp/efi-root
ExclusiveArch: ia64

%description
This package contains development headers and libraries for developing
applications that run under EFI (Extensible Firmware Interface).

%prep
%setup
%patch -p1
%patch2 -p1

%build
make CFLAGS="$RPM_OPT_FLAGS"

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README apps
/usr/include/efi
/usr/lib/*

%changelog
* Tue Dec  5 2000 Bill Nottingham <notting@redhat.com>
- update to 1.1

* Thu Oct 26 2000 Bill Nottingham <notting@redhat.com>
- add patch for new toolchain, update to 1.0

* Thu Aug 17 2000 Bill Nottingham <notting@redhat.com>
- update to 0.9
