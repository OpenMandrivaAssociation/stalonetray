%define name	stalonetray
%define version	0.8.0
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Stand-alone, full-featured system tray
Version: 	%{version}
Release: 	%{release}

Source:		%{name}-%{version}.tar.bz2
Patch0:		stalonetray-0.8.0-fix-str-fmt.patch
URL:		http://stalonetray.sourceforge.net/
License:	GPLv2
Group:		Graphical desktop/Other
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	X11-devel

%description
Stalonetray is a stand-alone freedesktop.org and KDE system tray (notification
area) for X Window System/X11. It has full XEMBED support and minimal
dependencies: an X11 lib only. Stalonetray works with virtually any
EWMH-compliant window manager.

%prep
%setup -q
%patch0 -p1 -b .strfmt

%build
%configure
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS TODO stalonetrayrc.sample %name.html
%{_bindir}/%name
%{_mandir}/man1/*
