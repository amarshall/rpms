Name:      cpuset
Version:   1.6
Release:   1%{?dist}
Summary:   Wrapper for Linux kernel cpusets
License:   GPLv2
URL:       https://github.com/lpechacek/cpuset
Source0:   https://github.com/lpechacek/cpuset/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch: noarch

Requires: python3

BuildRequires: python3-devel

%description
Wrapper for Linux kernel cpusets

%prep
%autosetup

%build
%py3_build

%install
%py3_install -- --prefix=%{_prefix} --install-data=/deleteme
rm -rf %{buildroot}/deleteme
mkdir -p %{buildroot}/%{_defaultdocdir}/%{name}/html
%{__install} -m 0444 doc/*.html %{buildroot}/%{_defaultdocdir}/%{name}/html
%{__install} -m 0444 NEWS README %{buildroot}/%{_defaultdocdir}/%{name}
mkdir -p %{buildroot}/%{_mandir}/man1
%{__install} -m 0444 doc/*.1 %{buildroot}/%{_mandir}/man1

%files
%doc %{_docdir}/%{name}
%license COPYING
%{_bindir}/cset
%{python3_sitelib}/*
%{_mandir}/man1/*
