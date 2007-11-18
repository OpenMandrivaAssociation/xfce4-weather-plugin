%define oname xfce4-weather-plugin
 
Summary:	A weather plugin for the Xfce panel
Name:		xfce-weather-plugin
Version:	0.6.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-weather-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-weather-plugin/xfce4-weather-plugin-%{version}.tar.bz2
Requires:	xfce-panel >= 4.3.0
BuildRequires:	xfce-panel-devel >= 4.3.0
BuildRequires:	libxfcegui4-devel >= 4.3
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-weather
Provides:	xfce-weather
Obsoletes:	xfce-weather-panel
Provides:	xfce-weather-panel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This panel plugin shows the current temperature and weather condition, 
using weather data provided by xoap.weather.com (www.weather.com).

%prep
%setup -qn %{oname}-%{version}

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 
 
%find_lang %{oname}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{oname}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog INSTALL README
%dir %{_datadir}/xfce4/weather
%{_datadir}/xfce4/weather/*
%{_datadir}/xfce4/panel-plugins/*
%{_libdir}/xfce4/panel-plugins/
%{_iconsdir}/hicolor/*/apps/*.png
