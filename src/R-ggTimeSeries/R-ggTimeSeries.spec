%global packname ggTimeSeries
%global rlibdir %{_datadir}/R/library

Name:      R-%{packname}
Version:   1.0.1
Release:   1%{?dist}
Summary:   Time series visualisations using the grammar of graphics

License:   MIT
URL:       https://CRAN.R-project.org/package=%{packname}
Source0:   https://cran.r-project.org/src/contrib/%{packname}_%{version}.tar.gz

BuildArch:     noarch
BuildRequires: R-devel
BuildRequires: tex(latex)
BuildRequires: R(data.table)
BuildRequires: R(ggplot2)
Requires:      R(data.table)
Requires:      R(ggplot2)

%description
Provides additional display mediums for time series visualisations, such as
calendar heat map, steamgraph, marimekko, etc.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/NEWS
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/R-ex
%{rlibdir}/%{packname}/help
