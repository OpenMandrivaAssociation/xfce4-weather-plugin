%define url_ver %(echo %{version} | cut -d. -f 1-2)
%define _disable_rebuild_configure 1

Summary:	A weather plugin for the Xfce panel
Name:		xfce4-weather-plugin
Version:	0.11.3
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		https://goodies.xfce.org/projects/panel-plugins/xfce4-weather-plugin
Source0:	https://archive.xfce.org/src/panel-plugins/xfce4-weather-plugin/%{url_ver}/%{name}-%{version}.tar.bz2
# from https://gitlab.xfce.org/panel-plugins/xfce4-weather-plugin/-/merge_requests/28
#Patch1:		28.diff
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gthread-2.0)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(json-c)
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(libxfce4panel-2.0)
BuildRequires:	pkgconfig(libxfce4ui-2)
BuildRequires:	pkgconfig(libxfce4util-1.0)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool

Requires:	xfce4-panel
Requires:	glib-networking
Obsoletes:	xfce-weather-plugin

%description
This panel plugin shows the current temperature and weather condition, 
using weather data provided by xoap.weather.com (www.weather.com).

%prep
%autosetup -p1

%build
autoreconf -fiv
%configure \
	--disable-static

%make_build

%install
%make_install

%find_lang %{name} %{name}.lang

%files -f %{name}.lang
%doc AUTHORS ChangeLog README
%dir %{_datadir}/xfce4/weather
%{_datadir}/xfce4/weather/*
%{_datadir}/xfce4/panel/plugins/*
%{_libdir}/xfce4/panel/plugins/
%{_iconsdir}/hicolor/*/apps/*.png
%{_iconsdir}/hicolor/scalable/apps/org.xfce.panel.weather.svg
