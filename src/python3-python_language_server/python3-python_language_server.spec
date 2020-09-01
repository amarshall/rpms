%define pkgname python_language_server
%define modname pyls
%define reponame python-language-server

Name:      python3-%{pkgname}
Version:   0.34.1
Release:   1%{?dist}
Summary:   An implementation of the Language Server Protocol for Python
License:   MIT
URL:       https://github.com/palantir/python-language-server
Source0:   %{url}/archive/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildArch: noarch
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires: python3-devel
Patch0: deps.patch

%description
An implementation of the Language Server Protocol for Python

%prep
%autosetup -p1 -n %{reponame}-%{version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{_bindir}/pyls
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{pkgname}-%{version}*-py*.egg-info
