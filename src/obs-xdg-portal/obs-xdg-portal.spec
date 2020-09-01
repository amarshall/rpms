%global _vpath_srcdir sdk/%{name}/projects/meson

Name:     obs-xdg-portal
Version:  0.1.2
Release:  1%{?dist}
Summary:  OBS Studio plugin using the Desktop portal for Wayland & X11 screencasting

License:  GPLv3
URL:      https://gitlab.gnome.org/feaneron/%{name}
Source:   %{url}/-/archive/%{version}/%{name}-%{version}.tar.gz

Requires: obs-studio-libs
BuildRequires: gcc
BuildRequires: meson
BuildRequires: obs-studio-devel

%description
OBS Studio plugin using the Desktop portal for Wayland & X11 screencasting

%prep
%autosetup -c

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%license COPYING
%{_libdir}/obs-plugins/lib%{name}.so.*
