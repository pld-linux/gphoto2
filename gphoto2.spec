# TODO:
#   make --enable-docs work.
#   library should be installed in /usr/lib.
Summary:	Digital camera software
Summary(pl):	Oprogramowanie dla kamer cyfrowych
Name:		gphoto2
Version:	2.1.0
Release:	5
License:	GPL
Group:		Applications
Source0:	http://prdownloads.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
Patch0:		%{name}-m4.patch
Patch1:		%{name}-am_ac.patch
URL:		http://www.gphoto.net/
BuildRequires:	XFree86-devel
BuildRequires:	aalib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	cdk-devel
BuildRequires:	findutils
BuildRequires:	gettext-devel
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libusb-devel
BuildRequires:	libtool >= 1.4.2-9
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%package lib-static
Summary:	Static version of gphoto2-lib
Summary(pl):	Statyczna wersja gphoto2-lib
Group:		Development/Libraries
Requires:	%{name}-lib-devel = %{version}
Obsoletes:	%{name}-static

%description lib-static
Static version of gphoto2-lib.

%description lib-static -l pl
Statyczna wersja gphoto2-lib.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
cd libgphoto2_port
rm -f missing
%{__libtoolize}
aclocal -I m4
%{__autoconf}
%{__automake}
cd ..

CPPFLAGS="-I/usr/include/cdk -I/usr/include/ncurses"
%configure CPPFLAGS="$CPPFLAGS"
	#--enable-docs --- doesn't build.
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

#install -d "$RPM_BUILD_ROOT%{_pkgconfigdir}"
#mv $RPM_BUILD_ROOT{%{_libdir}/pkgconfig,%{_pkgconfigdir}}

%find_lang %{name}
%find_lang libgphoto2_port

%clean
rm -rf $RPM_BUILD_ROOT

%post	lib -p /sbin/ldconfig
%postun	lib -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/gphoto2
%{_datadir}/%{name}
%{_mandir}/*/*

%files lib -f libgphoto2_port
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%dir %{_libdir}/gphoto2
%dir %{_libdir}/gphoto2/%{version}
%attr(755,root,root) %{_libdir}/gphoto2/%{version}/libgphoto2_*.??
%dir %{_libdir}/gphoto2_port
%dir %{_libdir}/gphoto2_port/0.5.0
%attr(755,root,root) %{_libdir}/gphoto2_port/0.5.0/libgphoto2_port_*.??

%files lib-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gphoto2-*
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/gphoto2
%{_pkgconfigdir}/*

%files lib-static
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/gphoto2/%{version}/lib*.a
%{_libdir}/gphoto2_port/0.5.0/lib*.a
