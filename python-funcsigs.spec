#
# Conditional build:
%bcond_without	doc	# don't build doc
%bcond_without	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module [not needed for Python 3.3+]

Summary:	Python function signatures from PEP362 for older Python versions
Summary(pl.UTF-8):	Sygnatury funkcji w Pythonie z PEP362 dla starszych wersji Pythona
Name:		python-funcsigs
Version:	0.4
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.python.org/pypi/funcsigs
Source0:	https://pypi.python.org/packages/source/f/funcsigs/funcsigs-%{version}.tar.gz
# Source0-md5:	fb1d031f284233e09701f6db1281c2a5
Patch0:		%{name}-no-unittest2.patch
URL:		https://pypi.python.org/pypi/funcsigs
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
BuildRequires:	python-setuptools
%if "%{py_ver}" < "2.7"
BuildRequires:	python-unittest2
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules >= 1:2.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
funcsigs module is a backport of the PEP 362 function signature
features from Python 3.3's inspect module. The backport is compatible
with Python 2.6, 2.7 as well as 3.2 and up.

%description -l pl.UTF-8
Moduł funcsigs to backport sygnatur funkcji PEP 362 z modułu inspect
Pythona 3.3. Jest zgodny z Pythonem 2.6, 2.7 oraz 3.2 i nowszymi.

%package -n python3-funcsigs
Summary:	Python function signatures from PEP362 for older Python versions
Summary(pl.UTF-8):	Sygnatury funkcji w Pythonie z PEP362 dla starszych wersji Pythona
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-funcsigs
funcsigs module is a backport of the PEP 362 function signature
features from Python 3.3's inspect module. The backport is compatible
with Python 2.6, 2.7 as well as 3.2 and up.

Note: in Python 3.3+ this functionality is available in inspect
module.

%description -n python3-funcsigs -l pl.UTF-8
Moduł funcsigs to backport sygnatur funkcji PEP 362 z modułu inspect
Pythona 3.3. Jest zgodny z Pythonem 2.6, 2.7 oraz 3.2 i nowszymi.

Uwaga: w Pythonie 3.3+ ta funkcjonalność jest dostępna w module
inspect.

%package apidocs
Summary:	API documentation for funcsigs module
Summary(pl.UTF-8):	Dokumentacja API modułu funcsigs
Group:		Documentation

%description apidocs
API documentation for funcsigs module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu funcsigs.

%prep
%setup -q -n funcsigs-%{version}
%if "%{py_ver}" >= "2.7"
%patch0 -p1
%endif

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%if %{with doc}
%{__make} -C docs -j1 html
%{__rm} -r docs/_build/html/{_sources,.buildinfo}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

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
%doc CHANGELOG LICENSE README.rst
%{py_sitescriptdir}/funcsigs
%{py_sitescriptdir}/funcsigs-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-funcsigs
%defattr(644,root,root,755)
%doc CHANGELOG LICENSE README.rst
%{py3_sitescriptdir}/funcsigs
%{py3_sitescriptdir}/funcsigs-%{version}-py*.egg-info
%endif

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc docs/_build/html/*
%endif
