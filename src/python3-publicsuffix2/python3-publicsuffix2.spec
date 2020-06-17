%define modname publicsuffix2
%define version0 2.2019-12-21
%define tarname python-%{modname}-release-%{version0}

Name:      python3-%{modname}
# Hyphens in version replaced with dots
Version:   2.20191221
Release:   1%{?dist}
Summary:   Get a public suffix for a domain name using the Public Suffix List
# Code under MIT, suffix list data under MPLv2.0
License:   MIT and MPLv2.0
URL:       https://github.com/nexb/python-publicsuffix2
Source0:   https://github.com/nexb/python-publicsuffix2/archive/release-%{version0}.tar.gz#/%{tarname}.tar.gz

BuildArch: noarch
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires: python3-devel
BuildRequires: python3dist(requests) >= 2.7.0

%description
Get a public suffix for a domain name using the Public Suffix List.

%prep
%autosetup -n %{tarname}

%build
%py3_build

%install
%py3_install

%files
%license publicsuffix2.LICENSE
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}-%{version}*-py*.egg-info
