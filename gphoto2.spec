Summary:	Command-line frontend to libgphoto2
Summary(es):	Foto GNU (gphoto) Release 2
Summary(pl):	Dzia³aj±cy z linii poleceñ program obs³uguj±cy libgphoto2
Summary(pt_BR):	GNU Photo - programa GNU para câmeras digitais
Summary(zh_CN):	gPhoto - LinuxÏÂµÄÊ¹ÓÃÊýÂëÏà»úµÄ³ÌÐò
Name:		gphoto2
Version:	2.1.5
Release:	0.1
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/gphoto/%{name}-%{version}.tar.gz
# Source0-md5:	9bd1a033389f9e4e6425dda4f6e603c9
#Patch0:		%{name}-manpage_addon.patch
Patch1:		%{name}-libexif069.patch
Patch2:		%{name}-locale_names.patch
URL:		http://www.gphoto.org/
BuildRequires:	aalib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cdk-devel
BuildRequires:	gettext-devel
BuildRequires:	libexif-devel
BuildRequires:	libgphoto2-devel >= 2.1.1
BuildRequires:	libjpeg-devel
BuildRequires:	pkgconfig
BuildRequires:	popt-devel
BuildRequires:	readline-devel
Requires:	libgphoto2 >= 2.1.1
#Requires:	dcraw
Obsoletes:	gphoto2-progs
# these are not true (renamed to libgphoto2-{devel,static}) - we must have
# the way to just rename package which is not required by anything installed
Obsoletes:	gphoto2-devel
Obsoletes:	gphoto2-static
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gphoto2 is a command-line frontend to libgphoto2.

%description -l es
Foto GNU (gphoto).

%description -l pl
gphoto2 to dzia³aj±cy z linii poleceñ program bêd±cy interfejsem
u¿ytkownika do libgphoto2.

%description -l pt_BR
O programa gphoto faz parte do projeto GNOME e é uma interface para
uma grande variedade de câmeras fotográficas digitais.

%prep
%setup -q
#%%patch0 -p1
#%patch1 -p1
%patch2 -p1

mv po/{no,nb}.po
mv po/{no,nb}.gmo

%build
cp -f /usr/share/automake/config.* .
CPPFLAGS="-I/usr/include/ncurses"
%{__aclocal}
%{__autoheader}
%{__autoconf}
%{__automake}
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
%doc ChangeLog README TODO
%attr(755,root,root) %{_bindir}/gphoto2
%{_mandir}/man1/*
