%global debug_package %{nil}

Name:      helm
Version:   3.6.0
Release:   1%{?dist}
Summary:   The Kubernetes Package Manager
License:   ASL 2.0
URL:       https://helm.sh
Source0:   https://github.com/helm/helm/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires: git
BuildRequires: golang
BuildRequires: make

%description
The Kubernetes Package Manager

%prep
%autosetup

%build
%make_build

%install
mkdir -p %{?buildroot}%{_bindir}
%make_install INSTALL_PATH=%{?buildroot}%{_bindir}

%check
%{buildroot}%{_bindir}/helm version

%files
%license LICENSE
%doc README.md
%{_bindir}/helm
