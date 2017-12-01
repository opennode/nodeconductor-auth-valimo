%define __conf_dir %{_sysconfdir}/waldur/valimo

Name: waldur-auth-valimo
Summary: Waldur Valimo authentication plugin
Group: Development/Libraries
Version: 0.3.1
Release: 1.el7
License: MIT
Url: http://waldur.com
Source0: %{name}-%{version}.tar.gz

Requires: waldur-core >= 0.151.0
Requires: python-lxml >= 3.2.0

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python-setuptools

%description
Waldur plugin bringing Valimo authentication support.

%prep
%setup -q -n %{name}-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --root=%{buildroot}

mkdir -p %{buildroot}%{__conf_dir}
echo "%{__conf_dir}" >> INSTALLED_FILES

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*

%changelog
* Fri Dec 1 2017 Jenkins <jenkins@opennodecloud.com> - 0.3.1-1.el7
- New upstream release

* Mon Nov 13 2017 Jenkins <jenkins@opennodecloud.com> - 0.3.0-1.el7
- New upstream release

* Mon Nov 13 2017 Victor Mireyev <victor@opennodecloud.com> - 0.2.0-1.el7
- Rename nodeconductor-auth-valimo package to waldur-auth-valimo.
