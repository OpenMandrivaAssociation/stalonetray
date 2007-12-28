%define name	stalonetray
%define version	0.7.5
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Stand-alone, full-featured system tray
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
URL:		http://stalonetray.sourceforge.net/
License:	GPL
Group:		Graphical desktop/Other
BuildRequires:	X11-devel

%description
Stalonetray is a stand-alone freedesktop.org and KDE system tray (notification
area) for X Window System/X11. It has full XEMBED support and minimal
dependencies: an X11 lib only. Stalonetray works with virtually any
EWMH-compliant window manager.

%prep
%setup -q

%build
%configure2_5x
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS TODO stalonetrayrc.sample %name.html
%{_bindir}/%name
%{_mandir}/man1/*
