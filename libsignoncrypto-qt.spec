# TODO: aegis-crypto (maemo platform)
Summary:	Encryption of DBus messages for signon-qt
Summary(pl.UTF-8):	Szyfrowanie komunikacji DBus dla signon-qt
Name:		libsignoncrypto-qt
Version:	1.3.1
Release:	1
License:	LGPL v2.1
Group:		Libraries
#Source0Download: http://code.google.com/p/accounts-sso/downloads/list
Source0:	http://accounts-sso.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	4bbeb8861569cf1008408adabc6d8df3
# fragments from http://depot.javispedro.com/nit/harm/srcs/pool/free/libs/libsignoncrypto-qt/libsignoncrypto-qt_1.3-1+0m8.diff.gz (changes existing on harmattan branch)
Patch0:		%{name}-harmattan.patch
URL:		http://code.google.com/p/accounts-sso/
BuildRequires:	QtCore-devel >= 4
BuildRequires:	doxygen
BuildRequires:	dbus-glib-devel
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	qt4-build >= 4
BuildRequires:	qt4-qmake >= 4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Encryption of DBus messages for signon-qt.

%description -l pl.UTF-8
Szyfrowanie komunikacji DBus dla signon-qt.

%package devel
Summary:	Development files for libsignoncrypto-qt library
Summary(pl.UTF-8):	Pliki programistyczne biblioteki libsignoncrypto-qt
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	QtCore-devel >= 4
Requires:	glib2-devel >= 2.0

%description devel
Development files for libsignoncrypto-qt library.

%description devel -l pl.UTF-8
Pliki programistyczne biblioteki libsignoncrypto-qt.

%package apidocs
Summary:	API documentation for libsignoncrypto-qt library
Summary(pl.UTF-8):	Dokumentacja API biblioteki libsignoncrypto-qt
Group:		Documentation

%description apidocs
API documentation for libsignoncrypto-qt library.

%description apidocs -l pl.UTF-8
Dokumentacja API biblioteki libsignoncrypto-qt.

%prep
%setup -q
%patch0 -p1

%build
qmake-qt4 libsignoncrypto-qt.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcxxflags}" \
	QMAKE_LFLAGS_RELEASE="%{rpmldflags}"

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

# useless symlink
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsignoncrypto-qt.so.1.?
# test suite
%{__rm} $RPM_BUILD_ROOT%{_bindir}/libsignoncrypto-qt-test
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/libsignoncrypto-qt-tests
# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libsignoncrypto-qt

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignoncrypto-qt.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsignoncrypto-qt.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsignoncrypto-qt.so
%{_includedir}/signoncrypto-qt
%{_pkgconfigdir}/libsignoncrypto-qt.pc

%files apidocs
%defattr(644,root,root,755)
%doc lib/doc/html/*
