# TODO:
#   make --enable-docs work.
#   library should be installed in /usr/lib.
Summary:	Digital camera software
Summary(pl):	Oprogramowanie dla kamer cyfrowych
Name:		gphoto2
Version:	2.0
Release:	0.5
License:	GPL
Group:		X11/Applications
Source0:	http://www.gphoto.net/dist/%{name}-%{version}.tar.gz
Patch0:		%{name}-m4.patch
Patch1:		%{name}-am_ac.patch
URL:		http://www.gphoto.net/
BuildRequires:	aalib-devel
BuildRequires:	bison
BuildRequires:	cdk-devel
BuildRequires:	findutils
BuildRequires:	gettext-devel
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libusb-devel
BuildRequires:	pkgconfig
BuildRequires:	libtool >= 1.4.2-9
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Digital camera software.

%description -l pl
Oprogramowanie dla kamer cyfrowych.

%package lib
Summary:	Libraries for digital cameras
Summary(pl):	Biblioteki obs³ugi kamer cyfrowych
Group:		Libraries

%description lib
Libraries for digital cameras.

%description lib -l pl
Biblioteki obs³ugi kamer cyfrowych.

%package static
Summary:	Static version of gphoto2-lib
Summary(pl):	Statyczna wersja gphoto2-lib
Group:		Development/Libraries

%description static
Static version of gphoto2-lib.

%description static -l pl
Statyczna wersja gphoto2-lib.

%package lib-devel
Summary:	Header files for gphoto2-lib
Summary(pl):	Pliki nag³ówkowe dla gphoto2-lib
Group:		Development/Libraries
Requires:	%{name}-lib = %{version}
Requires:	libexif-devel

%description lib-devel
Header files for gphoto2-lib.

%description lib-devel -l pl
Pliki nag³ówkowe dla gphoto2-lib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
install /usr/share/automake/missing .
libtoolize --copy --force
aclocal
%{__autoconf}
cd libgphoto2_port
install /usr/share/automake/missing .
libtoolize --copy --force
aclocal -I m4
%{__autoconf}
cd ..

CPPFLAGS="-I/usr/include/cdk -I/usr/include/ncurses"
%configure CPPFLAGS="$CPPFLAGS"
	#--enable-docs --- doesn't build.
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d "$RPM_BUILD_ROOT/%{_pkgconfigdir}"
mv $RPM_BUILD_ROOT{%{_libdir}/pkgconfig,%{_pkgconfigdir}}

gzip -9nf README ChangeLog

%find_lang %{name}
%find_lang libgphoto2_port

%post lib -p /sbin/ldconfig
%postun lib -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gphoto2
%{_datadir}/%{name}
%{_mandir}/*/*

%files lib -f libgphoto2_port
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_libdir}/*.so.*.*.*
%{_libdir}/gphoto2/2.0/libgphoto2_*.??
%{_libdir}/gphoto2_port/0.0.4/libgphoto2_port_*.??

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/gphoto2/2.0/libgphoto2_*.a
%{_libdir}/gphoto2_port/0.0.4/libgphoto2_port_*.a

%files lib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gphoto2-*
%{_includedir}/gphoto2
%{_libdir}/*.so
%{_pkgconfigdir}/*
