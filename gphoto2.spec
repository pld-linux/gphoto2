# TODO:
#   make --enable-docs work.
#   library should be installed in /usr/lib.
Summary:	Digital camera software
Summary(pl):	Oprogramowanie dla kamer cyfrowych
Name:		gphoto2
Version:	2.0
Release:	0.1
License:	GPL
Group:		X11/Applications
Source0:	http://www.gphoto.net/dist/gphoto2-2.0.tar.gz
Patch0:		%{name}-ncurses.patch
URL:		http://www.gphoto.net/
BuildRequires:	aalib-devel
BuildRequires:	bison
BuildRequires:	cdk-devel
BuildRequires:	gettext-devel
BuildRequires:	gtk-doc
BuildRequires:	libexif-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libusb-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description

%description -l pl

%package lib
Summary:	Libraries for digital cameras
Summary(pl):	Biblioteki obs³ugi kamer cyfrowych
Group:		Libraries
Requires:	%{name} = %{version}

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

%description lib-devel
Header files for gphoto2-lib.

%description lib-devel -l pl
Pliki nag³ówkowe dla gphoto2-lib.

%prep
%setup -q
#%patch0 -p1

%build
#autoconf
#cd libgphoto2_port
#autoconf
#cd ..

%configure2_13
	#--enable-docs --- doesn't build.
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

LD_LIBRARY_PATH="$RPM_BUILD_ROOT%{_libdir}"
export LD_LIBRARY_PATH

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d "$RPM_BUILD_ROOT/%{_pkgconfigdir}"
mv $RPM_BUILD_ROOT{/usr/X11R6/lib/pkgconfig,%{_pkgconfigdir}}

gzip -9nf README ChangeLog

%find_lang %{name}
%find_lang libgphoto2_port

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

%files lib -f libgphoto2_port
%defattr(644,root,root,755)
%{_libdir}/*.la
%{_libdir}/*.so.*.*.*

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files lib-devel
%defattr(644,root,root,755)
%{_includedir}/gphoto2
%{_libdir}/*.so
%{_pkgconfigdir}/*
