Name:           ngtcp2
Version:        1.8.0
Release:        %autorelease
Summary:        ngtcp2 project is an effort to implement RFC9000 QUIC protocol

License:        MIT
URL:            https://github.com/ngtcp2/ngtcp2
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  libtool
BuildRequires:  gnutls-devel

%description
"Call it TCP/2. One More Time."

ngtcp2 project is an effort to implement RFC9000 QUIC protocol.

%package devel
Summary:        ngtcp2 development files
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description devel
"Call it TCP/2. One More Time."

ngtcp2 project is an effort to implement RFC9000 QUIC protocol.

Development headers and libraries.

%prep
%autosetup


%build
autoreconf -fsi
%configure --with-gnutls --disable-static --enable-werror
%make_build


%install
%make_install


%files
%license COPYING
%doc README.rst
%doc SECURITY.md
%doc AUTHORS
%{_libdir}/libngtcp2.so.16*
%{_libdir}/libngtcp2_crypto_gnutls.so.8*


%files devel
%{_libdir}/libngtcp2.so
%{_libdir}/libngtcp2_crypto_gnutls.so
%{_libdir}/pkgconfig/libngtcp2.pc
%{_libdir}/pkgconfig/libngtcp2_crypto_gnutls.pc
%{_includedir}/%{name}/


%changelog
%autochangelog
