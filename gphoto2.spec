Summary:	Command-line frontend to libgphoto2
Summary(es.UTF-8):	Foto GNU (gphoto) Release 2
Summary(pl.UTF-8):	Działający z linii poleceń program obsługujący libgphoto2
Summary(pt_BR.UTF-8):	GNU Photo - programa GNU para câmeras digitais
Summary(zh_CN.UTF-8):	gPhoto - Linux下的使用数码相机的程序
Name:		gphoto2
Version:	2.4.7
Release:	1
License:	LGPL v2+
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# Source0-md5:	a0bd7629040735f16e510b63edf386dd
Patch0:		%{name}-manpage_addon.patch
Patch1:		%{name}-am.patch
URL:		http://www.gphoto.org/
BuildRequires:	aalib-devel
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	cdk-devel >= 5.0_td20010421
BuildRequires:	gettext-devel >= 0.14.1
BuildRequires:	libexif-devel >= 0.6.9
BuildRequires:	libgphoto2-devel >= 2.4.5
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	readline-devel
Requires:	libgphoto2 >= 2.4.7
Obsoletes:	gphoto2-progs
# these are not true (renamed to libgphoto2-{devel,static}) - we must have
# the way to just rename package which is not required by anything installed
Obsoletes:	gphoto2-devel
Obsoletes:	gphoto2-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gphoto2 is a command-line frontend to libgphoto2.

%description -l pl.UTF-8
gphoto2 to działający z linii poleceń program będący interfejsem
użytkownika do libgphoto2.

%description -l pt_BR.UTF-8
O programa gphoto faz parte do projeto GNOME e é uma interface para
uma grande variedade de câmeras fotográficas digitais.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

rm -f po/stamp-po

%build
%{__libtoolize}
%{__aclocal} -I auto-m4 -I m4m
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-I/usr/include/ncurses"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gphoto2
%{_mandir}/man1/gphoto2.1*
