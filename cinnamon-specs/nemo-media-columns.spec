Name:		nemo-media-columns
Version:	2.8.0
Summary:	A media column extension for nemo
Release:	%mkrel 1
License:	GPLv2+
URL:		https://github.com/linuxmint/nemo-extensions
Group:		Graphical desktop/Cinnamon
Source:		nemo-media-columns-%{version}.tar.xz
BuildRequires:	pkgconfig(glib-2.0) 
BuildRequires:	pkgconfig(gio-2.0)
BuildRequires:  pkgconfig(gobject-2.0) 
BuildRequires:	nemo-devel
Requires:	nemo 

%description
media columns extension for Nemo for the Cinnamon desktop environment. 


%prep
%setup -q -n nemo-media-columns-%{version}


%install
install -dm755 "%{buildroot}/usr/share/nemo-python/extensions/"
install -m644 nemo-media-columns.py \
                "%{buildroot}/usr/share/nemo-python/extensions/"

%files 
%defattr(-,root,root)
%{_datadir}/nemo-python/extensions/*


%changelog
* Sat Oct 26 2016 Mank <mank at pclinuxos dot cz> 2.8.0-1mank2016
- Create pkg


