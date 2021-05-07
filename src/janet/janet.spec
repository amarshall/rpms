%global debug_package %{nil}

Name:      janet
Version:   1.15.5
Release:   1%{?dist}
Summary:   A functional and imperative programming language
License:   MIT
URL:       https://github.com/janet-lang/janet
Source0:   %{url}/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: make
BuildRequires: gcc

%description
A functional and imperative programming language

%prep
%autosetup -p0

%build
%make_build

%install
export BINDIR=%{_bindir}
export LIBDIR=%{_libdir}
export PREFIX=%{_prefix}
%make_install
find %{buildroot} -type f

%check
make test

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%{_bindir}/jpm
%{_includedir}/%{name}/%{name}.h
%{_libdir}/lib%{name}.a
%{_libdir}/lib%{name}.so
%{_libdir}/lib%{name}.so.*
%{_libdir}/pkgconfig/%{name}.pc
%{_mandir}/man1/*
