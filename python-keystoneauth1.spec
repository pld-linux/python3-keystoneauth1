#
# TODO:
#	- enable 'extras' - kerberos and betamax (both require new dependecies)

# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_with	tests	# unit tests (require tons of dependencies)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Authentication Library for OpenStack Identity
Summary(pl.UTF-8):	Biblioteka uwierzytleniająca dla tożsamości OpenStack
Name:		python-keystoneauth1
# keep 3.x here for python2 support
Version:	3.18.0
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/k/keystoneauth1/keystoneauth1-%{version}.tar.gz
# Source0-md5:	6104205044175fa8aac659582fdd0260
URL:		https://docs.openstack.org/keystoneauth/latest/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-pbr >= 3.0.0
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-PyYAML >= 3.12
BuildRequires:	python-betamax >= 0.7.0
BuildRequires:	python-fixtures >= 3.0.0
BuildRequires:	python-iso8601 >= 0.1.11
BuildRequires:	python-lxml >= 3.4.1
BuildRequires:	python-mock >= 2.0.0
BuildRequires:	python-oauthlib >= 0.6.2
BuildRequires:	python-os-service-types >= 1.2.0
BuildRequires:	python-oslo.config >= 5.2.0
BuildRequires:	python-oslo.utils >= 3.33.0
BuildRequires:	python-oslotest >= 3.2.0
BuildRequires:	python-requests >= 2.14.2
BuildRequires:	python-requests-kerberos >= 0.8.0
BuildRequires:	python-requests-mock >= 1.2.0
BuildRequires:	python-six >= 1.10.0
BuildRequires:	python-stestr >= 1.0.0
BuildRequires:	python-stevedore >= 1.20.0
BuildRequires:	python-testresources >= 2.0.0
BuildRequires:	python-testtools >= 2.2.0
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-pbr >= 3.0.0
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-PyYAML >= 3.12
BuildRequires:	python3-betamax >= 0.7.0
BuildRequires:	python3-fixtures >= 3.0.0
BuildRequires:	python3-iso8601 >= 0.1.11
BuildRequires:	python3-lxml >= 3.4.1
BuildRequires:	python3-oauthlib >= 0.6.2
BuildRequires:	python3-os-service-types >= 1.2.0
BuildRequires:	python3-oslo.config >= 5.2.0
BuildRequires:	python3-oslo.utils >= 3.33.0
BuildRequires:	python3-oslotest >= 3.2.0
BuildRequires:	python3-requests >= 2.14.2
BuildRequires:	python3-requests-kerberos >= 0.8.0
BuildRequires:	python3-requests-mock >= 1.2.0
BuildRequires:	python3-six >= 1.10.0
BuildRequires:	python3-stestr >= 1.0.0
BuildRequires:	python3-stevedore >= 1.20.0
BuildRequires:	python3-testresources >= 2.0.0
BuildRequires:	python3-testtools >= 2.2.0
%endif
%endif
%if %{with doc}
BuildRequires:	python-openstackdocstheme >= 1.18.1
BuildRequires:	python-reno >= 2.5.0
BuildRequires:	python-sphinxcontrib-apidoc >= 0.2.0
BuildRequires:	sphinx-pdg-2 >= 1.7.0
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains tools for authenticating to an OpenStack-based
cloud. These tools include:
- Authentication plugins (password, token, and federation based)
- Discovery mechanisms to determine API version support
- A session that is used to maintain client settings across requests
  (based on the requests Python library)

%description -l pl.UTF-8
Ten pakiet zawiera narzędzia do uwierzytelniania do chmury opartej na
szkielecie OpenStack. Zawierają:
- wtyczki uwierzytelniające (oparte na hasłach, tokenach i
  federacjach)
- mechanizmy wykrywania do określania obsługi wersji API
- sesję, używaną do utrzymywania ustawień klienta między żądaniami
  (w oparciu o bibliotekę Pythona requests)

%package -n python3-keystoneauth1
Summary:	Authentication Library for OpenStack Identity
Summary(pl.UTF-8):	Biblioteka uwierzytleniająca dla tożsamości OpenStack
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.6

%description -n python3-keystoneauth1
This package contains tools for authenticating to an OpenStack-based
cloud. These tools include:
- Authentication plugins (password, token, and federation based)
- Discovery mechanisms to determine API version support
- A session that is used to maintain client settings across requests
  (based on the requests Python library)

%description -n python3-keystoneauth1 -l pl.UTF-8
Ten pakiet zawiera narzędzia do uwierzytelniania do chmury opartej na
szkielecie OpenStack. Zawierają:
- wtyczki uwierzytelniające (oparte na hasłach, tokenach i
  federacjach)
- mechanizmy wykrywania do określania obsługi wersji API
- sesję, używaną do utrzymywania ustawień klienta między żądaniami
  (w oparciu o bibliotekę Pythona requests)

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
%{__make} -C doc html \
	SPHINXBUILD=sphinx-build-2
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/keystoneauth1/tests
%endif

%if %{with python3}
%py3_install

%{__rm} -r $RPM_BUILD_ROOT%{py3_sitescriptdir}/keystoneauth1/tests
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
%doc doc/build/html/{_static,api,*.html,*.js}
%endif
