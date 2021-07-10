%define pkgname pyls-mypy
%define modname pyls_mypy
%define reponame pyls-mypy

Name:      python3-%{pkgname}
Version:   0.1.8
Release:   1%{?dist}
Summary:   Mypy plugin for the Python Language Server
License:   MIT
URL:       https://github.com/tomv564/pyls-mypy
Source0:   %{url}/archive/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
Patch0:    version.patch
Patch1:    future.patch

BuildArch: noarch
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Mypy plugin for the Python Language Server

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
export VERSION=%{version}
%py3_build

%install
export VERSION=%{version}
%py3_install

%files
%license LICENSE
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}-%{version}*-py*.egg-info
