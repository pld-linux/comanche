Summary:	A front-end for configuring the Apache Web server
Summary(pl):	Frontend do konfiguracji serwera WWW Apache
Name:		comanche
Version:	3
%define		_rc      b4
Release:	0%{_rc}
License:	GPL
Group:		Applications/System
Source0:	http://www.comanche.org/downloads/comanche%{version}.%{release}-src.tar.gz
# Source0-md5:	3f0a8eab0b16dbe05bbea95b72a23551
#Source0:	com%{version}.tar.gz
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Source3:	%{name}-mini.xpm
Requires:	itcl
Requires:	rcs
Requires:	tk
Obsoletes:	apachecfg
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Comanche (COnfiguration MANager for apaCHE) is a front-end for the
Apache Web server, the most popular Web server used on the Internet.
Comanche aims to to make it easier to manage and configure Apache.

Install the commanche package if you need a configuration manager for
the Apache Web server. You'll also need to install the apache package.

%description -l pl
Commanche (COnfiguration MANager for apaCHE) jest interfejsem
(frontendem) dla Apache, najpopularniejszego serwera WWW u¿ywanego w
sieci Internet. Dziêki Commanche ³atwiej jest zarz±dzaæ i konfigurowaæ
Apache.

%prep
%setup -q -n comanche%{version}-%{release}

%build
cat > comanche.sh <<EOF
#!/bin/sh
#

cd %{_prefix}/lib/comanche
exec %{_bindir}/itkwish3.0 main.tcl %{_sysconfdir}/httpd/conf
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_prefix}/lib/comanche,%{_pixmapsdir}/mini,%{_desktopdir}}

install comanche.sh $RPM_BUILD_ROOT%{_bindir}
rm -f apachectl INSTALL changes.txt comanche.sh
cp -a * $RPM_BUILD_ROOT%{_prefix}/lib/comanche
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/mini/mini-comanche.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_prefix}/lib/comanche
%{_desktopdir}/comanche.desktop
%{_pixmapsdir}/comanche.xpm
%{_pixmapsdir}/mini
