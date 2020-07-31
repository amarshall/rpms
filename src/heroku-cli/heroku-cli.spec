Name:      heroku-cli
Version:   7.47.10
Release:   1%{?dist}
Summary:   Heroku CLI
License:   ISC
URL:       https://devcenter.heroku.com/articles/heroku-cli
Source0:   https://cli-assets.heroku.com/heroku-linux-x64.tar.gz#/heroku.tar.gz

BuildArch: noarch

BuildRequires: nodejs
Requires: nodejs

%description
Heroku CLI

%prep
%autosetup -n heroku
rm bin/heroku.cmd bin/node
find . -mindepth 1 -name '.*' -print0 | xargs -0 rm -r
find . -empty -delete
find node_modules -type f -print0 | xargs -0 chmod -x

%build
# Interpretted

%install
mkdir -p %{buildroot}/%{_datarootdir}/%{name} %{buildroot}/%{_bindir}
cp -r . %{buildroot}/%{_datarootdir}/%{name}
rm %{buildroot}/%{_datarootdir}/%{name}/CHANGELOG.md
rm %{buildroot}/%{_datarootdir}/%{name}/LICENSE
rm %{buildroot}/%{_datarootdir}/%{name}/README.md
ln -s --relative %{buildroot}/%{_datarootdir}/%{name}/bin/heroku %{buildroot}/%{_bindir}/heroku

%check
%{buildroot}/%{_bindir}/heroku --version

%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{_bindir}/heroku
%{_datadir}/%{name}/
