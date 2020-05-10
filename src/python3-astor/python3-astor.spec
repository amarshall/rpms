%define modname astor

Name:      python3-%{modname}
Version:   0.8.1
Release:   1%{?dist}
Summary:   Easy manipulation of Python source via the AST
License:   BSD
URL:       https://astor.readthedocs.io/en/stable
Source0:   https://github.com/berkerpeksag/astor/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz

BuildArch: noarch
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires: python3-devel

%description
Easy manipulation of Python source via the AST.

%prep
%autosetup -n %{modname}-%{version}

%build
%py3_build

%install
%py3_install

%files
%license LICENSE
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}-%{version}*-py*.egg-info
