Summary:	A weather plugin for the Xfce panel
Name:		xfce4-weather-plugin
Version:	0.6.2
Release:	%mkrel 6
License:	GPLv2+
Group:		Graphical desktop/Xfce
URL:		http://goodies.xfce.org/projects/panel-plugins/xfce4-weather-plugin
Source0:	http://goodies.xfce.org/releases/xfce4-weather-plugin/%{name}-%{version}.tar.bz2
Patch0:		01_save_config.patch
Patch1:		%{name}-0.6.2-fix-utf8-encodings.patch
Patch2:		%{name}-0.6.2-resolv-support.patch
Patch3:		xfce4-weather-plugin-0.6.2-libtool-fixes.patch
Patch4:		xfce4-weather-plugin-0.6.2-fix_display_orientation.patch
Patch5:		xfce4-weather-plugin-0.6.2-adapt_to_gtk_2.12_api.patch
BuildRequires:	xfce4-panel-devel >= 4.4.2
BuildRequires:	libxfcegui4-devel >= 4.4.2
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
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
# (tpg) needed for patch2
xdt-autogen

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
