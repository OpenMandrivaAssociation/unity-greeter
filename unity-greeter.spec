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

Provides: lightdm-greeter

%description
A LightDM greeter for the Unity Desktop Environment.

%prep
%setup -q

%build
%configure2_5x \
	--disable-static

%make LIBS='-lX11'

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%config(noreplace) %{_sysconfdir}/lightdm/unity-greeter.conf
%{_sbindir}/unity-greeter
%{_datadir}/unity-greeter
%{_datadir}/xgreeters/unity-greeter.desktop

