Summary:	A front-end for configuring the Apache Web server.
Name:		comanche
Version:	990405
Release:	3
Group:		Utilities/System
Group(pl):	Narzêdzia/System
Source0:	http://comanche.com.dtu.dk/comanche/download/com%{version}.tar.gz
Source1:	comanche.wmconfig
Source2:	comanche.xpm
Source3:	comanche-mini.xpm
License:	GPL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	apachecfg
Requires:	itcl, tk, rcs
BuildArchitectures:	noarch

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
%setup -q -n com%{version}

%build
cat > comanche <<EOF
#!/bin/bash
#

cd %{_libdir}/comanche
exec %{_bindir}/itkwish3.0 main.tcl %{_sysconfdir}/httpd/conf
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/comanche,%{_datadir}/icons/mini}
install -d $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig

install comanche $RPM_BUILD_ROOT%{_bindir}
rm apachectl INSTALL changes.txt comanche 
cp -a * $RPM_BUILD_ROOT%{_libdir}/comanche
install $RPM_SOURCE_DIR/comanche.wmconfig $RPM_BUILD_ROOT%{_sysconfdir}/X11/wmconfig/comanche
install $RPM_SOURCE_DIR/comanche.xpm $RPM_BUILD_ROOT%{_datadir}/icons
install $RPM_SOURCE_DIR/comanche-mini.xpm \
	$RPM_BUILD_ROOT%{_datadir}/icons/mini/mini-comanche.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/comanche
%attr(600,root,root) %config(missingok) %{_sysconfdir}/X11/wmconfig/comanche
%{_datadir}/icons/comanche.xpm
%{_datadir}/icons/mini/mini-comanche.xpm
