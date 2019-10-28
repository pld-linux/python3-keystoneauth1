#
# TODO:
#	- enable 'extras' - kerberos and betamax (both require new dependecies)

# Conditional build:
%bcond_with	doc	# build doc
%bcond_with	tests	# do perform "make test" (requires tons of dependencies)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Authentication Library for OpenStack Identity
Name:		python-keystoneauth1
Version:	3.1.0
Release:	3
License:	Apache
Group:		Libraries/Python
Source0:	https://pypi.python.org/packages/60/84/563732a068310ee9a8c3626a037efea22b3a926431d91f1ec991db89a70e/keystoneauth1-%{version}.tar.gz
# Source0-md5:	ddfb0d140292a22969b4bcbe08e5df12
URL:		https://docs.openstack.org/keystoneauth/latest/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-pbr >= 2.0.0
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-pbr >= 2.0.0
BuildRequires:	python3-setuptools
%endif
Requires:	python-iso8601 >= 0.1.11
Requires:	python-pbr >= 2.0.0
Requires:	python-positional >= 1.1.1
Requires:	python-requests >= 2.14.2
Requires:	python-six >= 1.9.0
Requires:	python-stevedore >= 1.20.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains tools for authenticating to an OpenStack-based
cloud. These tools include:

- Authentication plugins (password, token, and federation based)
- Discovery mechanisms to determine API version support
- A session that is used to maintain client settings across requests
  (based on the requests Python library)

%package -n python3-keystoneauth1
Summary:	Authentication Library for OpenStack Identity
Group:		Libraries/Python
Requires:	python3-iso8601 >= 0.1.11
Requires:	python3-modules
Requires:	python3-pbr >= 2.0.0
Requires:	python3-positional >= 1.1.1
Requires:	python3-requests >= 2.14.2
Requires:	python3-six >= 1.9.0
Requires:	python3-stevedore >= 1.20.0

%description -n python3-keystoneauth1
This package contains tools for authenticating to an OpenStack-based
cloud. These tools include:

- Authentication plugins (password, token, and federation based)
- Discovery mechanisms to determine API version support
- A session that is used to maintain client settings across requests
  (based on the requests Python library)

%package apidocs
Summary:	API documentation for Python keystoneauth1 module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona keystoneauth1
Group:		Documentation

%description apidocs
API documentation for Pythona keystoneauth1 module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona keystoneauth1.

%prep
%setup -q -n keystoneauth1-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
cd doc
%{__make} -j1 html
rm -rf _build/html/_sources
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

# when files are installed in other way that standard 'setup.py
# they need to be (re-)compiled
# change %{py_sitedir} to %{py_sitescriptdir} for 'noarch' packages!
%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py_sitescriptdir}/keystoneauth1
%{py_sitescriptdir}/keystoneauth1-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-keystoneauth1
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README.rst
%{py3_sitescriptdir}/keystoneauth1
%{py3_sitescriptdir}/keystoneauth1-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
