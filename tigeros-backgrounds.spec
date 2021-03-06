Name:           tigeros-backgrounds
Version:        1.0
Release:        16%{?dist}
Summary:        Desktop wallpapers for the TigerOS Fedora Remix

Group:          Applications/Multimedia
License:        CC-BY-SA-4.0
URL:            https://github.com/RITlug/TigerOS
Source0:        %{name}.tar.gz

BuildArch:      noarch
Requires:       glib2
Requires:       dconf

%description
The tigeros-backgrounds package contains
tigeros related artwork intended to be used 
as a desktop background image.

%prep
%setup -q

%install
mkdir -p %{buildroot}%{_datadir}/backgrounds/tigeros
mkdir -p %{buildroot}%{_datadir}/glib-2.0/schemas

for i in wallpapers/*
do
	install -m 644 $i %{buildroot}%{_datadir}/backgrounds/tigeros
done

install -D -m 644 tigeros-backgrounds.xml %{buildroot}%{_datadir}/gnome-background-properties/tigeros-backgrounds.xml
install -m 644 20_tigeros.gschema.override %{buildroot}%{_datadir}/glib-2.0/schemas/20_tigeros.gschema.override

%post
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null
dconf update

%postun
glib-compile-schemas /usr/share/glib-2.0/schemas 2>/dev/null
dconf update

%files
%defattr(-,root,root,-)
%doc LICENSE
%{_datadir}/backgrounds
%{_datadir}/gnome-background-properties
%{_datadir}/glib-2.0/schemas/20_tigeros.gschema.override

%changelog
* Wed Aug 30 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-16
- rebuilt for Fedora 26

* Wed May 31 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-15
- fix typo in wallpaper override

* Thu May 25 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-14
- add wallpaper override

* Sun May 14 2017 Aidan Kahrs <axk4545@rit.edu> - 1.0-13
- fix xml so wallpapers are zoomed

* Wed Apr 26 2017 Regina Locicero <rtl3971@rit.edu> - 1.0-12
- Added wallpapers
