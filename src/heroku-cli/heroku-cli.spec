Name:      heroku-cli
Version:   7.42.6
Release:   1%{?dist}
Summary:   Heroku CLI
License:   ISC
URL:       https://devcenter.heroku.com/articles/heroku-cli
Source0:   https://cli-assets.heroku.com/heroku-linux-x64.tar.gz#/heroku.tar.gz

BuildArch: noarch

BuildRequires: nodejs
Requires: nodejs

%description
Git command plugin to list recently checked-out branches in the current repository

%prep
%autosetup -n heroku
rm bin/heroku.cmd bin/node

%build
# Interpretted

%install
mkdir -p %{buildroot}/%{_datarootdir} %{buildroot}/%{_bindir}
cp -r . %{buildroot}/%{_datarootdir}/
ln -s %{buildroot}/%{_datarootdir}/bin/heroku %{buildroot}/%{_bindir}/heroku

%check
test "$(%{buildroot}/%{_bindir}/heroku --version | grep --only-matching '^Heroku/[0-9.]+ ')" = 'Heroku/%{version} '

%files
%license LICENSE
%doc CHANGELOG.md
%doc README.md
%{_bindir}/heroku
%{_datarootdir}/heroku
