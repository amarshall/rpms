%define modname hy

Name:      python3-%{modname}
Version:   0.18.0
Release:   1%{?dist}
Summary:   A dialect of Lisp that’s embedded in Python
License:   MIT
URL:       https://docs.hylang.org/en/stable
Source0:   https://github.com/hylang/hy/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz
Patch0:    requires.patch

BuildArch: noarch
%{?python_provide:%python_provide python3-%{modname}}
BuildRequires: python3-devel

%description
A dialect of Lisp that’s embedded in Python

%prep
%autosetup -p1 -n %{modname}-%{version}
echo "__version__ = '%{version}'" > hy/version.py

%build
%py3_build

%install
export HY_VERSION=%{version}
%py3_install
rm %{buildroot}/%{_prefix}/get_version/get_version.py
rm %{buildroot}/%{_bindir}/hy2py3
rm %{buildroot}/%{_bindir}/hy3
rm %{buildroot}/%{_bindir}/hyc3

%files
%license LICENSE
%{_bindir}/hy
%{_bindir}/hy2py
%{_bindir}/hyc
%{python3_sitelib}/%{modname}
%{python3_sitelib}/%{modname}-%{version}*-py*.egg-info
