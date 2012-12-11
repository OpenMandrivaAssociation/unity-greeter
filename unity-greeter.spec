Summary:	LightDM Unity Greeter
Name:		unity-greeter
Version:	0.2.8
Release:	1
Group:		System/X11
License:	GPLv3
URL:		https://launchpad.net/unity-greeter
Source0:	https://launchpad.net/unity-greeter/+download/%{name}-%{version}.tar.gz

BuildRequires:	intltool
BuildRequires:	pkgconfig(liblightdm-gobject-1)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(indicator3-0.4)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	vala
BuildRequires:	vala-devel

Provides: lightdm-greeter

%description
A LightDM greeter for the Unity Desktop Environment.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make LIBS='-lX11 -lm'

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%files -f %{name}.lang
%{_sbindir}/unity-greeter
%{_datadir}/unity-greeter
%{_datadir}/xgreeters/unity-greeter.desktop
%{_datadir}/glib-2.0/schemas/*.gschema.xml


%changelog
* Fri May 18 2012 Crispin Boylan <crisb@mandriva.org> 0.2.8-1
+ Revision: 799538
- New release

* Fri Mar 02 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.1.1-1
+ Revision: 781832
- imported package unity-greeter

