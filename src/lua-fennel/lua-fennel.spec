%global luapkgdir %{_datadir}/lua/%{luaver}

%global pkgname fennel
%global reponame Fennel

Name:           lua-%{pkgname}
Version:        0.4.1
Release:        1%{?dist}
Summary:        A Lisp-family programming language which compiles to Lua.

License:        MIT
URL:            https://fennel-lang.org
Source0:        https://github.com/bakpakin/%{reponame}/archive/%{version}.tar.gz#/%{reponame}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  lua >= 5.1
BuildRequires:  lua-filesystem
BuildRequires:  make
Requires:       lua(abi)


%description
Fennel is a programming language that brings together the speed, simplicity,
and reach of Lua with the flexibility of a lisp syntax and macro system.


%prep
%autosetup -n %{reponame}-%{version}


%build
%make_build fennel
sed -i 's@^#!/usr/bin/env lua$@#!/usr/bin/lua@' fennel


%install
%{__install} -D -m 0755 fennel -t %{buildroot}%{_bindir}
%{__install} -D -m 0644 fennel.lua fennelfriend.lua fennelview.lua -t %{buildroot}%{luapkgdir}
%{__install} -D -m 0644 fennel.1 -t %{buildroot}%{_mandir}/man1


%files
%license LICENSE
%doc changelog.md README.md tutorial.md
%{_bindir}/fennel
%{_mandir}/man1/*
%{luapkgdir}/fennel.lua
%{luapkgdir}/fennelfriend.lua
%{luapkgdir}/fennelview.lua
