# TODO:
#   make --enable-docs work.
#   library should be installed in /usr/lib.
#
Summary:	Libraries for digital cameras
Summary(es):	Foto GNU (gphoto) Release 2
Summary(pl):	Biblioteki obs³ugi kamer cyfrowych
Summary(pt_BR):	GNU Photo - programa GNU para câmeras digitais
Name:		gphoto2
Version:	2.1.0
Release:	9
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# Source0-md5:	b998bcb01cbb1916dedea03b7119ae42
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
Obsoletes:	gphoto2-lib
Provides:	gphoto2-lib

%description
Libraries for digital cameras.

%description -l es
Foto GNU (gphoto).

%description -l pl
Biblioteki obs³ugi kamer cyfrowych.

%description -l pt_BR
O programa gphoto faz parte do projeto GNOME e é uma interface para
uma grande variedade de câmeras fotográficas digitais.

%package progs
Summary:	Digital camera software
Summary(pl):	Oprogramowanie dla kamer cyfrowych
Group:		Libraries
Requires:	%{name} >= %{version}

%description progs
Digital camera software.

%description progs -l pl
Oprogramowanie dla kamer cyfrowych.

%package devel
Summary:	Header files for gphoto2
Summary(es):	Archivos de deserrolo de gphoto2
Summary(pl):	Pliki nag³ówkowe dla gphoto2
Summary(pt_BR):	Arquivos de desenvolvimento do gphoto2
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libexif-devel
Obsoletes:	gphoto2-lib-devel

%description devel
Header files for gphoto2.

%description devel -l es
Archivos de desarrolo de gphoto2.

%description devel -l pl
Pliki nag³ówkowe dla gphoto2.

%description devel -l pt_BR
Arquivos de desenvolvimento do gphoto2.

%package static
Summary:	Static version of gphoto2
Summary(es):	Archivos de deserrolo de gphoto2
Summary(pl):	Statyczna wersja gphoto2
Summary(pt_BR):	Arquivos de desenvolvimento do gphoto2
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}
Obsoletes:	gphoto2-lib-static

%description static
Static version of gphoto2.

%description static -l es
Archivos de desarrolo de gphoto2.

%description static -l pl
Statyczna wersja gphoto2.

%description static -l pt_BR
Arquivos de desenvolvimento do gphoto2.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
cd libgphoto2_port
rm -f missing
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
cd ..

CPPFLAGS="-I/usr/include/cdk -I/usr/include/ncurses"
%configure CPPFLAGS="$CPPFLAGS"
	#--enable-docs --- doesn't build.
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

for f in $RPM_BUILD_ROOT%{_datadir}/locale/{da,it,no,ru,sl,uk}/LC_MESSAGES/libgphoto_port.mo ; do
	[ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] && rm -f $f
done
%find_lang %{name}
%find_lang libgphoto2_port

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f libgphoto2_port.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/*.so.*.*.*
%dir %{_libdir}/gphoto2
%dir %{_libdir}/gphoto2/%{version}
%attr(755,root,root) %{_libdir}/gphoto2/%{version}/libgphoto2_*.??
%dir %{_libdir}/gphoto2_port
%dir %{_libdir}/gphoto2_port/0.5.0
%attr(755,root,root) %{_libdir}/gphoto2_port/0.5.0/libgphoto2_port_*.??

%files progs -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/gphoto2
%{_datadir}/%{name}
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gphoto2-*
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
%{_includedir}/gphoto2
%{_pkgconfigdir}/*
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
%{_libdir}/gphoto2/%{version}/lib*.a
%{_libdir}/gphoto2_port/0.5.0/lib*.a
