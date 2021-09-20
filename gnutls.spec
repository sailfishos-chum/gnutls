Name:           gnutls37
Version:        3.7.2
Release:        1%{?dist}
Summary:        A TLS protocol implementation

License:        GPLv3+ and LGPLv2+
URL:            https://www.gnutls.org
Source0:        gnutls-%{version}.tar.xz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  p11-kit-devel
BuildRequires:  libtasn1-devel
BuildRequires:  nettle-devel
BuildRequires:  gmp-devel
BuildRequires:  m4
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  gettext-devel
BuildRequires:  texinfo

Requires(post): coreutils
Requires(postun): coreutils

%package c++
Summary: The C++ interface to GnuTLS
Requires: %{name}%{?_isa} = %{version}-%{release}

%package devel
Summary: Development files for the %{name} package
Requires: %{name}%{?_isa} = %{version}-%{release}
Requires: %{name}-c++%{?_isa} = %{version}-%{release}
Requires: pkgconfig
Conflicts: gnutls-devel

%package utils
License: GPLv3+
Summary: Command line tools for TLS protocol
Requires: %{name}%{?_isa} = %{version}-%{release}

%description
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS
protocols and technologies around them. It provides a simple C language
application programming interface (API) to access the secure communications
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and
other required structures.

%description c++
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS
protocols and technologies around them. It provides a simple C language
application programming interface (API) to access the secure communications
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and
other required structures.

%description devel
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS
protocols and technologies around them. It provides a simple C language
application programming interface (API) to access the secure communications
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and
other required structures.
This package contains files needed for developing applications with
the GnuTLS library.

%description utils
GnuTLS is a secure communications library implementing the SSL, TLS and DTLS
protocols and technologies around them. It provides a simple C language
application programming interface (API) to access the secure communications
protocols as well as APIs to parse and write X.509, PKCS #12, OpenPGP and
other required structures.
This package contains command line TLS client and server and certificate
manipulation tools.

%prep
%setup -q -n gnutls-%{version}

%build
%configure --with-included-unistring
%make_build

%install
%make_install
rm -f $RPM_BUILD_ROOT/%{_docdir}/gnutls/*.png
rm -rf $RPM_BUILD_ROOT/%{_datadir}/locale

%post
/sbin/ldconfig

%post c++
/sbin/ldconfig

%postun
/sbin/ldconfig

%postun c++
/sbin/ldconfig

%files
%{_libdir}/libgnutls.so.30*
%doc README.md AUTHORS NEWS THANKS
%license LICENSE doc/COPYING doc/COPYING.LESSER

%files c++
%{_libdir}/libgnutlsxx.so.28*

%files devel
%{_includedir}/*
%{_libdir}/libgnutls*.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man3/*
%{_infodir}/gnutls*
%{_infodir}/pkcs11-vision*

%files utils
%{_bindir}/certtool
%{_bindir}/ocsptool
%{_bindir}/psktool
%{_bindir}/p11tool
%{_bindir}/srptool
%{_bindir}/gnutls*
%{_mandir}/man1/*
%doc doc/certtool.cfg

%changelog
* Mon Sep 20 2021 Renaud Casenave-Péré <renaud@casenave-pere.fr> - 3.7.2-1
- Initial version
