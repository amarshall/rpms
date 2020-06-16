%define modname mitmproxy
%define modname_pathod pathod

Name:      python3-%{modname}
Version:   5.1.1
Release:   1%{?dist}
Summary:   An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers
License:   MIT
URL:       https://mitmproxy.org
Source0:   https://github.com/mitmproxy/mitmproxy/archive/v%{version}.tar.gz#/%{modname}-%{version}.tar.gz

BuildArch: noarch
%{?python_provide:%python_provide python3-%{modname}}
%{?python_provide:%python_provide python3-%{modname_pathod}}
BuildRequires: python3-devel

%description
An interactive TLS-capable intercepting HTTP proxy for penetration testers and software developers.

%prep
%autosetup -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{_bindir}/mitmdump
%{_bindir}/mitmproxy
%{_bindir}/mitmweb
%{_bindir}/pathoc
%{_bindir}/pathod
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}-%{version}*-py*.egg-info
%{python3_sitelib}/%{modname_pathod}
