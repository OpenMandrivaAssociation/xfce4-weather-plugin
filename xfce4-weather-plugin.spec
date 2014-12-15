%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A weather plugin for the Xfce panel
Name:		xfce4-weather-plugin
Version:	0.8.4
Release:	1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-weather-plugin
Source0:	http://archive.xfce.org/src/panel-plugins/xfce4-weather-plugin/0.8/%{name}-%{version}.tar.bz2
Patch0:		xfce4-weather-plugin-0.8.3-fix-linking.patch
BuildRequires:	pkgconfig(libxfce4panel-1.0)
BuildRequires:	pkgconfig(libxfce4ui-1) >= 4.7.0
BuildRequires:	pkgconfig(libsoup-2.4)
BuildRequires:	pkgconfig(upower-glib)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-weather-plugin

%description
This panel plugin shows the current temperature and weather condition, 
using weather data provided by xoap.weather.com (www.weather.com).

%prep
%setup -q
%apply_patches

%build
NOCONFIGURE=1 xdt-autogen

%configure2_5x \
	--disable-static

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
