Summary: A front-end for configuring the Apache Web server.
Name: comanche
Serial: 1
Version: 990405
Release: 2
Group: Applications/System
Source0: http://comanche.com.dtu.dk/comanche/download/com%{version}.tar.gz
Source1: comanche.wmconfig
Source2: comanche.xpm
Source3: comanche-mini.xpm

Copyright: GPL
BuildRoot: /var/tmp/comanche-root
BuildArchitectures: noarch
Obsoletes: apachecfg
Requires: itcl, tk, rcs

%description
Comanche (COnfiguration MANager for apaCHE) is a front-end for the
Apache Web server, the most popular Web server used on the Internet.
Comanche aims to to make it easier to manage and configure Apache.

Install the commanche package if you need a configuration manager for
the Apache Web server. You'll also need to install the apache package.

%prep
%setup -q -n com%{version}

%build
cat > comanche <<EOF
#!/bin/bash
#

cd /usr/lib/comanche
exec /usr/bin/itkwish3.0 main.tcl /etc/httpd/conf
EOF

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,lib/comanche}
mkdir -p $RPM_BUILD_ROOT/etc/X11/wmconfig
install -m 755 comanche $RPM_BUILD_ROOT/usr/bin
rm apachectl INSTALL changes.txt comanche 
cp -a * $RPM_BUILD_ROOT/usr/lib/comanche
install -m 644 $RPM_SOURCE_DIR/comanche.wmconfig $RPM_BUILD_ROOT/etc/X11/wmconfig/comanche
chmod 600 $RPM_BUILD_ROOT/etc/X11/wmconfig/comanche
mkdir -p $RPM_BUILD_ROOT/usr/share/icons/mini
install -m 644 $RPM_SOURCE_DIR/comanche.xpm $RPM_BUILD_ROOT/usr/share/icons
install -m 644 $RPM_SOURCE_DIR/comanche-mini.xpm \
	$RPM_BUILD_ROOT/usr/share/icons/mini/mini-comanche.xpm

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/*
/usr/lib/comanche
%config(missingok) /etc/X11/wmconfig/comanche
/usr/share/icons/comanche.xpm
/usr/share/icons/mini/mini-comanche.xpm
