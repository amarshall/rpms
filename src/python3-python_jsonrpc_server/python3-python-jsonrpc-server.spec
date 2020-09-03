%define pkgname python_jsonrpc_server
%define modname pyls_jsonrpc
%define reponame python-jsonrpc-server

Name:      python3-%{pkgname}
Version:   0.3.4
Release:   1%{?dist}
Summary:   A Python 2.7 and 3.4+ server implementation of the JSON RPC 2.0 protocol
License:   MIT
URL:       https://github.com/palantir/%{reponame}
Source0:   %{url}/archive/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
Patch0:    version.patch
Patch1:    deps.patch

BuildArch: noarch
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires: python3-devel

%description
A Python 2.7 and 3.4+ server implementation of the JSON RPC 2.0 protocol

%prep
%autosetup -p1 -n %{reponame}-%{version}
rm pyls_jsonrpc/_version.py
rm versioneer.py
sed -i 's@\$VERSION\$@%{version}@' setup.py
sed -i 's@\$VERSION\$@%{version}@' pyls_jsonrpc/__init__.py

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{pkgname}-%{version}*-py*.egg-info
