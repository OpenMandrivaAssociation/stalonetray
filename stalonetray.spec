Name: 	 	stalonetray
Summary: 	Stand-alone, full-featured system tray
Version: 	0.8.1
Release: 	1

Source:		%{name}-%{version}.tar.bz2
Patch0:		stalonetray-0.8.0-fix-str-fmt.patch
URL:		http://stalonetray.sourceforge.net/
License:	GPLv2
Group:		Graphical desktop/Other
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
%configure2_5x
%make
										
%install
rm -rf %{buildroot}
%makeinstall_std

%check
%make check

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog README NEWS TODO stalonetrayrc.sample %name.html
%{_bindir}/%name
%{_mandir}/man1/*


%changelog
* Sat Oct 22 2011 Matthew Dawkins <mattydaw@mandriva.org> 0.8.1-1
+ Revision: 705633
- new version 0.8.1

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.8.0-3mdv2011.0
+ Revision: 614975
- the mass rebuild of 2010.1 packages

* Thu Dec 31 2009 Jérôme Brenier <incubusss@mandriva.org> 0.8.0-2mdv2010.1
+ Revision: 484269
+ rebuild (emptylog)

* Thu Dec 31 2009 Jérôme Brenier <incubusss@mandriva.org> 0.8.0-1mdv2010.1
+ Revision: 484260
- new version 0.8.0
- fix str fmt
- fix license tag
- use %%configure instead of %%configure2_5x
- $RPM_BUILD_ROOT -> %%{buildroot}

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sat Aug 02 2008 Thierry Vignaud <tv@mandriva.org> 0.7.6-4mdv2009.0
+ Revision: 261032
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.7.6-3mdv2009.0
+ Revision: 253197
- rebuild

* Fri Jan 18 2008 Austin Acton <austin@mandriva.org> 0.7.6-1mdv2008.1
+ Revision: 154504
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Dec 28 2007 Austin Acton <austin@mandriva.org> 0.7.5-1mdv2008.1
+ Revision: 138717
- new version

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Jun 09 2007 Austin Acton <austin@mandriva.org> 0.6.5-1mdv2008.0
+ Revision: 37735
- Import stalonetray

