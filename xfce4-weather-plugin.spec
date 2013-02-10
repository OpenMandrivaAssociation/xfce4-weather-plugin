%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A weather plugin for the Xfce panel
Name:		xfce4-weather-plugin
Version:	0.8.2
Release:	2
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-weather-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-weather-plugin/%{url_ver}/%{name}-%{version}.tar.bz2

# Patch0 from Arch Linux:
# https://bugzilla.xfce.org/show_bug.cgi?id=8105
# https://bugs.archlinux.org/task/26815
Patch0:		xfce4-weather-plugin-0.7.4-working-XOAP-license-key.patch

BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	libxfce4util-devel
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.7.0
BuildRequires:	libxml2-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-weather-plugin

%description
This panel plugin shows the current temperature and weather condition, 
using weather data provided by xoap.weather.com (www.weather.com).

%prep
%setup -q
#patch0 -p0

%build
%configure2_5x
%make

%install
%makeinstall_std

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%dir %{_datadir}/xfce4/weather
%{_datadir}/xfce4/weather/*
%{_datadir}/xfce4/panel/plugins/*
%{_libdir}/xfce4/panel/plugins/
%{_iconsdir}/hicolor/*/apps/*.png


%changelog
* Tue Apr 17 2012 Crispin Boylan <crisb@mandriva.org> 0.7.4-5
+ Revision: 791573
- Rebuild

* Sun Apr 08 2012 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.4-4
+ Revision: 789866
- rebuild
- drop old stuff from spec file

* Tue Feb 21 2012 Jon Dill <dillj@mandriva.org> 0.7.4-3
+ Revision: 778765
- rebuild against new version of libffi4

* Mon Nov 21 2011 Sergio Rafael Lemke <sergio@mandriva.com> 0.7.4-2
+ Revision: 732176
- Added patch to fix the 'no data' on the panel applet

* Sat Mar 12 2011 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.4-1
+ Revision: 644045
- update to new version 0.7.4
- update url for Source0
- tune up buildrequires

* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 0.7.3-3mdv2011.0
+ Revision: 615651
- the mass rebuild of 2010.1 packages

* Fri May 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.3-2mdv2010.1
+ Revision: 543443
- rebuild for mdv 2010.1

* Wed Aug 05 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.3-1mdv2010.0
+ Revision: 409651
- update to new version 0.7.3

* Wed Jul 29 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.2-1mdv2010.0
+ Revision: 404018
- update to new version 0.7.2

* Wed Jul 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.1-1mdv2010.0
+ Revision: 398599
- update to new version 0.7.1

* Wed Jun 24 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.7.0-1mdv2010.0
+ Revision: 388886
- update to new version 0.7.0
- drop patch 0

* Tue Jun 16 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.4-1mdv2010.0
+ Revision: 386436
- update to new version 0.6.4

* Sun Jun 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.3-1mdv2010.0
+ Revision: 385908
- update to new version 0.6.3
- drop patches 1,2,3,4 and 5, they were merged by upstream

* Thu Jun 11 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-6mdv2010.0
+ Revision: 385033
- Patch2: better version
- Patch4: fix display orientation
- Patch5: take advantage of new gtk-2.12 tooltips

* Sun Mar 22 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-5mdv2009.1
+ Revision: 360451
- Patch3: fixes against latest libtool

* Sat Oct 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-4mdv2009.1
+ Revision: 295033
- rebuild for new Xfce4.6 beta1

* Sat Jun 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-3mdv2009.0
+ Revision: 229726
- Patch1: fix UTF8 encodings
- Patch2: add resolvconf support (upstream bug #4118)

* Wed Apr 16 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-2mdv2009.0
+ Revision: 194689
- Patch0: save nicely units

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.2-1mdv2008.1
+ Revision: 110578
- new version

* Mon Nov 19 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.1-1mdv2008.1
+ Revision: 110143
- correct buildrequires
- new license policy
- use upstream tarball name as a real name
- do not package COPYING and INSTALL files
- use upstream name
- new license policy
- new version

* Fri May 25 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-3mdv2008.0
+ Revision: 31037
- add %%post and %%postun scripts

* Thu May 24 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-2mdv2008.0
+ Revision: 30499
- update url
- spec file clean

* Wed May 23 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-1mdv2008.0
+ Revision: 30295
- new version

