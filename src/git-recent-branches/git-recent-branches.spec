Name:      git-recent-branches
Version:   0.3.2
Release:   1%{?dist}
Summary:   Git command plugin to list recently checked-out branches in the current repository
License:   MIT
URL:       https://github.com/amarshall/git-recent-branches
Source0:   https://github.com/amarshall/git-recent-branches/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:    env.patch

BuildArch: noarch

BuildRequires: make
Requires: ruby

%description
Git command plugin to list recently checked-out branches in the current repository

%prep
%autosetup -p0

%build
# Interpretted

%install
%make_install prefix=/usr

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
