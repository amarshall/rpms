%global debug_package %{nil}

%global reponame ChezScheme
%global nanopass_reponame nanopass-framework-scheme
%global nanopass_version 1.9
%global zlib_reponame zlib
%global zlib_version 1.2.11
%global stex_reponame stex
%global stex_version 1.2.1

Name:     chez-scheme
Version:  9.5.2
Release:  1%{?dist}
Summary:  Superset of R6RS Scheme programming language implementation.
License:  ASL 2.0
URL:      https://cisco.github.io/ChezScheme
Source0:  https://github.com/cisco/%{reponame}/archive/v%{version}.tar.gz#/%{reponame}-%{version}.tar.gz
Source1:  https://github.com/nanopass/%{nanopass_reponame}/archive/v%{nanopass_version}.tar.gz#/%{nanopass_reponame}-%{nanopass_version}.tar.gz
Source2:  https://github.com/madler/%{zlib_reponame}/archive/v%{zlib_version}.tar.gz#/%{zlib_reponame}-%{zlib_version}.tar.gz
Source3:  https://github.com/dybvig/%{stex_reponame}/archive/v%{stex_version}.tar.gz#/%{stex_reponame}-%{stex_version}.tar.gz

BuildRequires: gcc
BuildRequires: pkgconfig(ncurses)
BuildRequires: pkgconfig(uuid)
BuildRequires: pkgconfig(x11)

%description
Chez Scheme is both a programming language and an implementation of that
language, with supporting tools and documentation.

As a superset of the language described in the Revised6 Report on the
Algorithmic Language Scheme (R6RS), Chez Scheme supports all standard features
of Scheme, including first-class procedures, proper treatment of tail calls,
continuations, user-defined records, libraries, exceptions, and hygienic macro
expansion.

%prep
%autosetup -n %{reponame}-%{version}
%setup -q -D -T -a 1 -n %{reponame}-%{version}
%setup -q -D -T -a 2 -n %{reponame}-%{version}
%setup -q -D -T -a 3 -n %{reponame}-%{version}
rm -r nanopass stex zlib
mv %{nanopass_reponame}-%{nanopass_version} nanopass
mv %{stex_reponame}-%{stex_version} stex
mv %{zlib_reponame}-%{zlib_version} zlib
test -f nanopass/nanopass.ss
test -f stex/Mf-stex
test -f zlib/configure

%build
%{_configure} \
  --threads \
  --installprefix=%{_prefix} \
  --installbin=%{_bindir} \
  --installlib=%{_libdir} \
  --installman=%{_mandir} \
  --installschemename=chez \
  --installpetitename=petite \
  --installscriptname=chez-script \
  --temproot=%{buildroot}
%make_build

%install
%make_install
chmod --recursive u+rw,g+r,o+r %{buildroot}/%{_bindir} %{buildroot}/%{_libdir}

%files
%defattr(-,root,root)
%doc README.md
%license LICENSE NOTICE
%{_bindir}/chez
%{_bindir}/chez-script
%{_bindir}/petite
%{_libdir}/csv%{version}
%{_mandir}/man1/*
