Summary:	Command-line frontend to libgphoto2
Summary(pl):	Dzia³aj±cy z linii poleceñ program obs³uguj±cy libgphoto2
Name:		gphoto2
Version:	2.1.1
Release:	1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# Source0-md5: ce77b9c9ce25a57990c61f9e301e74b9
URL:		http://www.gphoto.net/
BuildRequires:	aalib-devel
BuildRequires:	cdk-devel
BuildRequires:	gettext-devel
BuildRequires:	libexif-devel
BuildRequires:	libgphoto2-devel >= 2.1.1
BuildRequires:	libjpeg-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	readline-devel
Requires:	libgphoto2 >= 2.1.1
Obsoletes:	gphoto2-progs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gphoto2 is a command-line frontend to libgphoto2.

%description -l pl
gphoto2 to dzia³aj±cy z linii poleceñ program bêd±cy interfejsem
u¿ytkownika do libgphoto2.

%prep
%setup -q

%build
#CPPFLAGS="-I/usr/include/cdk -I/usr/include/ncurses"
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
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/gphoto2
%{_mandir}/man1/*
