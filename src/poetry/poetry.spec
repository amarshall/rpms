%global pypi_name poetry

%global common_description %{expand:
Poetry helps you declare, manage and install dependencies of Python
projects, ensuring you have the right stack everywhere.}

Name:           %{pypi_name}
Summary:        Python dependency management and packaging made easy
Version:        1.0.10
Release:        10%{?dist}
License:        MIT

URL:            https://poetry.eustace.io/
Source0:        %{pypi_source}

# relax some too-strict dependencies that are specified in setup.py:
# - importlib-metadata (either removed or too old in fedora)
# - keyring (too new in fedora, but should be compatible)
# - pyrsistent (too new in fedora, but should be compatible)
# - requests-toolbelt (too new in fedora, but should be compatible)
Patch0:         00-setup-requirements-fixes.patch
Patch1:         01-54870697d921ae6efdbba0bc86f6b54c86d6896a.patch

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

Requires:       python3-%{pypi_name} = %{version}-%{release}

%description %{common_description}


%package -n     python3-%{pypi_name}
Summary:        %{summary}

# this is an optional dependency of CacheControl, but it's required by poetry
Requires:       python3dist(lockfile)

%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name} %{common_description}


%prep
%autosetup -p1


%build
%py3_build


%install
%py3_install


%files
%license LICENSE
%doc README.md

%{_bindir}/poetry

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.md

%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info/
