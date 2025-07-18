#
# Conditional build:
%bcond_without	aalib	# AAlib support
#
Summary:	Command-line frontend to libgphoto2
Summary(es.UTF-8):	Foto GNU (gphoto) Release 2
Summary(pl.UTF-8):	Działający z linii poleceń program obsługujący libgphoto2
Summary(pt_BR.UTF-8):	GNU Photo - programa GNU para câmeras digitais
Summary(zh_CN.UTF-8):	gPhoto - Linux下的使用数码相机的程序
Name:		gphoto2
Version:	2.5.28
Release:	1
License:	LGPL v2+
Group:		Applications/Graphics
Source0:	http://downloads.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# Source0-md5:	e7b3c835c26e2a5e61cf0b95e19da507
Patch0:		%{name}-pl.po-update.patch
URL:		http://www.gphoto.org/
%{?with_aalib:BuildRequires:	aalib-devel}
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1:1.9
BuildRequires:	cdk-devel >= 5.0_td20010421
BuildRequires:	gettext-tools >= 0.14.1
BuildRequires:	libexif-devel >= 1:0.6.9
BuildRequires:	libgphoto2-devel >= 2.5.17
BuildRequires:	libjpeg-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	popt-devel >= 1.6.1
BuildRequires:	readline-devel
Requires:	libexif >= 1:0.6.9
Requires:	libgphoto2 >= 2.5.17
Requires:	popt >= 1.6.1
Obsoletes:	gphoto2-progs < 2.1.1
# these are not true (renamed to libgphoto2-{devel,static}) - we must have
# the way to just rename package which is not required by anything installed
Obsoletes:	gphoto2-devel < 2.1.1
Obsoletes:	gphoto2-static < 2.1.1
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
%patch -P0 -p1

%{__rm} po/stamp-po

%build
%{__libtoolize}
%{__aclocal} -I auto-m4 -I gphoto-m4
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="%{rpmcppflags} -I/usr/include/ncurses"
%configure \
	%{?with_aalib:--with-aalib}
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
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/gphoto2
%{_mandir}/man1/gphoto2.1*
