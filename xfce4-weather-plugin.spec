%define url_ver %(echo %{version} | cut -c 1-3)

Summary:	A weather plugin for the Xfce panel
Name:		xfce4-weather-plugin
Version:	0.7.4
Release:	5
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
BuildRequires:	libxml2-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	intltool
Requires:	xfce4-panel >= 4.4.2
Obsoletes:	xfce-weather-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This panel plugin shows the current temperature and weather condition, 
using weather data provided by xoap.weather.com (www.weather.com).

%prep
%setup -q
%patch0 -p0

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
%{_datadir}/xfce4/panel-plugins/*
%{_libdir}/xfce4/panel-plugins/
%{_iconsdir}/hicolor/*/apps/*.png
