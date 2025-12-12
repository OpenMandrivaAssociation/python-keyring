%define pypi_name	keyring

Name:		python-keyring
Summary:	Python library to access the system keyring service
Version:	25.6.0
Release:	2
Group:		Development/Python
License:	Python
URL:		https://pypi.org/project/keyring/
Source0:	https://files.pythonhosted.org/packages/source/k/keyring/keyring-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(tomli)
#BuildRequires:  python-importlib-metadata
BuildRequires:	python%{pyver}dist(jeepney)
BuildRequires:	python%{pyver}dist(secretstorage)
BuildRequires:	python-pip
BuildRequires:	python-wheel

#Requires:	python3dist(pygobject)
%{?python_provide:%python_provide python3-keyring}

%patchlist

%description
The Python keyring lib provides a easy way to access the system keyring
service from python. It can be used in any application that needs safe
password storage.

This package only provides file-based pseudo-keyrings. To interface with
KWallet or gnome-keyring, please install one of python-keyring-kwallet or
python-keyring-gnome.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%build
%py_build

%install
%py_install

%files
%license LICENSE
%doc README.rst NEWS.rst
%{python_sitelib}/*.dist-info
%{python_sitelib}/%{pypi_name}
%{_bindir}/keyring
