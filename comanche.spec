Summary:	A front-end for configuring the Apache Web server
Summary(pl):	Frontend do konfiguracji serwera WWW Apache
Name:		comanche
Version:	990405
Release:	3
License:	GPL
Group:		Applications/System
Source0:	http://comanche.com.dtu.dk/comanche/download/com%{version}.tar.gz
# Source0-md5:	cdfcfb009411ff33a0090b1314a66396
Source1:	%{name}.desktop
Source2:	%{name}.xpm
Source3:	%{name}-mini.xpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	apachecfg
Requires:	itcl, tk, rcs
BuildArch:	noarch

%description
Comanche (COnfiguration MANager for apaCHE) is a front-end for the
Apache Web server, the most popular Web server used on the Internet.
Comanche aims to to make it easier to manage and configure Apache.

Install the commanche package if you need a configuration manager for
the Apache Web server. You'll also need to install the apache package.

%description -l pl
Commanche (COnfiguration MANager for apaCHE) jest interfejsem
(frontendem) dla Apache, najpopularniejszego serwera WWW u�ywanego w
sieci Internet. Dzi�ki Commanche �atwiej jest zarz�dza� i konfigurowa�
Apache.

%prep
%setup -q -n com%{version}

%build
cat > comanche <<EOF
#!/bin/sh
#

cd %{_libdir}/comanche
exec %{_bindir}/itkwish3.0 main.tcl %{_sysconfdir}/httpd/conf
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/comanche,%{_pixmapsdir}/mini,%{_applnkdir}/System}

install comanche $RPM_BUILD_ROOT%{_bindir}
rm -f apachectl INSTALL changes.txt comanche
cp -a * $RPM_BUILD_ROOT%{_libdir}/comanche
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/System
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}
install %{SOURCE3} $RPM_BUILD_ROOT%{_pixmapsdir}/mini/mini-comanche.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/comanche
%{_applnkdir}/System/comanche.desktop
%{_pixmapsdir}/comanche.xpm
%{_pixmapsdir}/mini/mini-comanche.xpm
