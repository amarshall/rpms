Name:      adwaita-cursor-theme-ext
Version:   0.1.0
Release:   1%{?dist}
Summary:   Fixes for some “missing” cursors in Adwaita
License:   MIT

BuildArch: noarch

Requires: adwaita-cursor-theme

%description
Fixes for some “missing” cursors in Adwaita

%prep

%build

%install
mkdir -p %{buildroot}/%{_datadir}/icons/Adwaita/cursors
cd %{buildroot}/%{_datadir}/icons/Adwaita/cursors
ln -s grab openhand

%files
%{_datadir}/icons/Adwaita/cursors/openhand
