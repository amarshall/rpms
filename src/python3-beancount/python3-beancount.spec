%define modname beancount
%global __requires_exclude ^python3[.0-9]*dist\\(python-magic\\)$

Name:      python3-%{modname}
Version:   2.2.3
Release:   1%{?dist}
Summary:   Double-entry accounting from text files
License:   GPLv2
URL:       https://beancount.github.io/docs
Source0:   https://github.com/beancount/beancount/archive/%{version}.tar.gz#/%{modname}-%{version}.tar.gz

%{?python_provide:%python_provide python3-%{modname}}
Requires: %{py3_dist file-magic}
BuildRequires: gcc
BuildRequires: python3-devel

%description
A double-entry bookkeeping computer language that lets you define financial
transaction records in a text file, read them in memory, generate a variety of
reports from them, and provides a web interface.

%prep
%autosetup -n %{modname}-%{version}
sed -i 's@^#!/usr/bin/env python[0-9.]*$@#!/usr/bin/python3@' bin/*

%build
%py3_build

%install
%py3_install
rm %{buildroot}/usr/elisp/beancount.el
rm %{buildroot}/%{_bindir}/upload-to-sheets

%files
%license COPYING
%{_bindir}/bean-bake
%{_bindir}/bean-check
%{_bindir}/bean-doctor
%{_bindir}/bean-example
%{_bindir}/bean-extract
%{_bindir}/bean-file
%{_bindir}/bean-format
%{_bindir}/bean-identify
%{_bindir}/bean-price
%{_bindir}/bean-query
%{_bindir}/bean-report
%{_bindir}/bean-sql
%{_bindir}/bean-web
%{_bindir}/treeify
%{python3_sitearch}/%{modname}
%{python3_sitearch}/%{modname}-%{version}*-py*.egg-info
