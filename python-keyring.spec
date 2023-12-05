%define pypi_name	keyring

Name:		python-keyring
Summary:	Python library to access the system keyring service
Version:	24.3.0
Release:	1
Group:		Development/Python
License:	Python
URL:		https://pypi.org/project/keyring/
Source0:	https://files.pythonhosted.org/packages/source/k/keyring/keyring-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(setuptools-scm)
BuildRequires:	python3dist(tomli)
#BuildRequires:  python-importlib-metadata
BuildRequires:	python3dist(jeepney)
BuildRequires:	python3dist(secretstorage)
BuildRequires:	python-pip
BuildRequires:	python-wheel

Requires:	python3dist(pygobject)
%{?python_provide:%python_provide python3-keyring}

%description
The Python keyring lib provides a easy way to access the system keyring
service from python. It can be used in any application that needs safe
password storage.

This package only provides file-based pseudo-keyrings. To interface with
KWallet or gnome-keyring, please install one of python-keyring-kwallet or
python-keyring-gnome.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# drop bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
mkdir wheels
pip wheel --wheel-dir wheels --no-deps --no-build-isolation --verbose .

%install
pip install --root=%{buildroot} --no-deps --verbose --ignore-installed --no-warn-script-location --no-index --no-cache-dir --find-links wheels wheels/*.whl

# we don't ship tests they need a test environment
rm -rf %{buildroot}%{python3_sitelib}/%{pypi_name}/tests/

%files
%license LICENSE
%doc README.rst NEWS.rst
%{python_sitelib}/*dist-info
%{python_sitelib}/%{pypi_name}
%{_bindir}/keyring
