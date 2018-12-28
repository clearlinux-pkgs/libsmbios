#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsmbios
Version  : 2.4.2
Release  : 11
URL      : https://github.com/dell/libsmbios/archive/v2.4.2.tar.gz
Source0  : https://github.com/dell/libsmbios/archive/v2.4.2.tar.gz
Summary  : C libraries for accessing dmi data
Group    : Development/Tools
License  : BSD-3-Clause GPL-2.0 OSL-2.0
Requires: libsmbios-bin
Requires: libsmbios-python3
Requires: libsmbios-lib
Requires: libsmbios-license
Requires: libsmbios-locales
Requires: libsmbios-man
Requires: libsmbios-data
Requires: libsmbios-python
BuildRequires : doxygen
BuildRequires : gettext
BuildRequires : graphviz
BuildRequires : help2man
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(libxml-2.0)

%description
We have decided to use a boost-style configuration system for libsmbios. The
headers in and below this directory are mostly imported from boost with all
"BOOST" prefixes changed to LIBSMBIOS.

%package bin
Summary: bin components for the libsmbios package.
Group: Binaries
Requires: libsmbios-data
Requires: libsmbios-license
Requires: libsmbios-man

%description bin
bin components for the libsmbios package.


%package data
Summary: data components for the libsmbios package.
Group: Data

%description data
data components for the libsmbios package.


%package dev
Summary: dev components for the libsmbios package.
Group: Development
Requires: libsmbios-lib
Requires: libsmbios-bin
Requires: libsmbios-data
Provides: libsmbios-devel

%description dev
dev components for the libsmbios package.


%package doc
Summary: doc components for the libsmbios package.
Group: Documentation
Requires: libsmbios-man

%description doc
doc components for the libsmbios package.


%package lib
Summary: lib components for the libsmbios package.
Group: Libraries
Requires: libsmbios-data
Requires: libsmbios-license

%description lib
lib components for the libsmbios package.


%package license
Summary: license components for the libsmbios package.
Group: Default

%description license
license components for the libsmbios package.


%package locales
Summary: locales components for the libsmbios package.
Group: Default

%description locales
locales components for the libsmbios package.


%package man
Summary: man components for the libsmbios package.
Group: Default

%description man
man components for the libsmbios package.


%package python
Summary: python components for the libsmbios package.
Group: Default
Requires: libsmbios-python3

%description python
python components for the libsmbios package.


%package python3
Summary: python3 components for the libsmbios package.
Group: Default
Requires: python3-core

%description python3
python3 components for the libsmbios package.


%prep
%setup -q -n libsmbios-2.4.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530580581
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1530580581
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libsmbios
cp COPYING-OSL %{buildroot}/usr/share/doc/libsmbios/COPYING-OSL
cp COPYING-GPL %{buildroot}/usr/share/doc/libsmbios/COPYING-GPL
cp COPYING %{buildroot}/usr/share/doc/libsmbios/COPYING
cp pkg/debian/copyright %{buildroot}/usr/share/doc/libsmbios/pkg_debian_copyright
cp doc/getopt/LICENSE %{buildroot}/usr/share/doc/libsmbios/doc_getopt_LICENSE
%make_install
%find_lang libsmbios

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/smbios-battery-ctl
/usr/bin/smbios-get-ut-data
/usr/bin/smbios-keyboard-ctl
/usr/bin/smbios-lcd-brightness
/usr/bin/smbios-passwd
/usr/bin/smbios-state-byte-ctl
/usr/bin/smbios-sys-info
/usr/bin/smbios-sys-info-lite
/usr/bin/smbios-thermal-ctl
/usr/bin/smbios-token-ctl
/usr/bin/smbios-upflag-ctl
/usr/bin/smbios-wakeup-ctl
/usr/bin/smbios-wireless-ctl

%files data
%defattr(-,root,root,-)
/usr/share/smbios-utils/__pycache__/cli.cpython-37.pyc
/usr/share/smbios-utils/cli.py
/usr/share/smbios-utils/token_blacklist.csv
/usr/share/smbios-utils/token_list.csv

%files dev
%defattr(-,root,root,-)
/usr/include/smbios_c/cmos.h
/usr/include/smbios_c/compat.h
/usr/include/smbios_c/config/abi/msvc_prefix.h
/usr/include/smbios_c/config/abi/msvc_suffix.h
/usr/include/smbios_c/config/abi_prefix.h
/usr/include/smbios_c/config/abi_suffix.h
/usr/include/smbios_c/config/auto_link.h
/usr/include/smbios_c/config/compiler/gcc.h
/usr/include/smbios_c/config/compiler/sunpro_cc.h
/usr/include/smbios_c/config/compiler/visualc.h
/usr/include/smbios_c/config/get_config.h
/usr/include/smbios_c/config/platform/linux.h
/usr/include/smbios_c/config/platform/win32.h
/usr/include/smbios_c/config/platform/win64.h
/usr/include/smbios_c/config/select_compiler_config.h
/usr/include/smbios_c/config/select_platform_config.h
/usr/include/smbios_c/config/suffix.h
/usr/include/smbios_c/config/user.h
/usr/include/smbios_c/memory.h
/usr/include/smbios_c/obj/cmos.h
/usr/include/smbios_c/obj/memory.h
/usr/include/smbios_c/obj/smbios.h
/usr/include/smbios_c/obj/smi.h
/usr/include/smbios_c/obj/token.h
/usr/include/smbios_c/smbios.h
/usr/include/smbios_c/smi.h
/usr/include/smbios_c/system_info.h
/usr/include/smbios_c/token.h
/usr/include/smbios_c/types.h
/usr/lib64/libsmbios_c.so
/usr/lib64/pkgconfig/libsmbios_c.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/libsmbios/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsmbios_c.so.2
/usr/lib64/libsmbios_c.so.2.2.1

%files license
%defattr(-,root,root,-)
/usr/share/doc/libsmbios/COPYING
/usr/share/doc/libsmbios/COPYING-GPL
/usr/share/doc/libsmbios/COPYING-OSL
/usr/share/doc/libsmbios/doc_getopt_LICENSE

%files man
%defattr(-,root,root,-)
/usr/share/man/man1/smbios-battery-ctl.1
/usr/share/man/man1/smbios-get-ut-data.1
/usr/share/man/man1/smbios-keyboard-ctl.1
/usr/share/man/man1/smbios-lcd-brightness.1
/usr/share/man/man1/smbios-passwd.1
/usr/share/man/man1/smbios-state-byte-ctl.1
/usr/share/man/man1/smbios-sys-info-lite.1
/usr/share/man/man1/smbios-sys-info.1
/usr/share/man/man1/smbios-thermal-ctl.1
/usr/share/man/man1/smbios-token-ctl.1
/usr/share/man/man1/smbios-upflag-ctl.1
/usr/share/man/man1/smbios-wakeup-ctl.1
/usr/share/man/man1/smbios-wireless-ctl.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files locales -f libsmbios.lang
%defattr(-,root,root,-)

