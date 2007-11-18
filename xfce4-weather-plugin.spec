Summary:	A weather plugin for the Xfce panel
Name:		xfce4-weather-plugin
Version:	0.6.1
Release:	%mkrel 1
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-weather-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-weather-plugin/%{name}-%{version}.tar.bz2
Requires:	xfce4-panel >= 4.4.2
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
BuildRequires:	perl(XML::Parser)
Obsoletes:	xfce-weather-plugin
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
This panel plugin shows the current temperature and weather condition, 
using weather data provided by xoap.weather.com (www.weather.com).

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std 
 
%find_lang %{name}

%post
%update_icon_cache hicolor

%postun
%clean_icon_cache hicolor

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog README
%dir %{_datadir}/xfce4/weather
%{_datadir}/xfce4/weather/*
%{_datadir}/xfce4/panel-plugins/*
%{_libdir}/xfce4/panel-plugins/
%{_iconsdir}/hicolor/*/apps/*.png
