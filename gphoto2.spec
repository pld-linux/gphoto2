Summary:	Command-line frontend to libgphoto2
Summary(es):	Foto GNU (gphoto) Release 2
Summary(pl):	Dzia�aj�cy z linii polece� program obs�uguj�cy libgphoto2
Summary(pt_BR):	GNU Photo - programa GNU para c�meras digitais
Summary(zh_CN):	gPhoto - Linux�µ�ʹ����������ĳ���
Name:		gphoto2
Version:	2.1.1
Release:	3
License:	GPL
Group:		Applications/Graphics
Source0:	http://dl.sourceforge.net/gphoto/%{name}-%{version}.tar.bz2
# Source0-md5: ce77b9c9ce25a57990c61f9e301e74b9
URL:		http://www.gphoto.org/
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

%description -l es
Foto GNU (gphoto).

%description -l pl
gphoto2 to dzia�aj�cy z linii polece� program b�d�cy interfejsem
u�ytkownika do libgphoto2.

%description -l pt_BR
O programa gphoto faz parte do projeto GNOME e � uma interface para
uma grande variedade de c�meras fotogr�ficas digitais.

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
