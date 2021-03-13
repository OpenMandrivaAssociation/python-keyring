%define pypi_name	keyring

Name:		python-keyring
Summary:	Python library to access the system keyring service
Version:	23.0.0
Release:	1
Group:		Development/Python
License:	Python
URL:		https://pypi.org/project/keyring/
Source0:	https://files.pythonhosted.org/packages/e8/3e/4daf55c21dc38dfa39a5780fb1c9a15dbbe8d680a715b0c81c29be51662c/keyring-%{version}.tar.gz
BuildArch:	noarch

BuildRequires:	pkgconfig(python)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(setuptools-scm)
BuildRequires:	python3dist(toml)
BuildRequires:  python-importlib-metadata
Requires:	python3dist(pygobject)
%{?python_provide:%python_provide python3-keyring}

%description
The Python keyring lib provides a easy way to access the system keyring
service from python. It can be used in any application that needs safe
password storage.

This package only provides file-based pseudo-keyrings. To interface with
gnome-keyring or KWallet, please install one of python-keyring-gnome or
python-keyring-kwallet.

%prep
%setup -q -n %{pypi_name}-%{version}

# drop bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py_build

%install
%py_install

# we don't ship tests they need a test environment
rm -rf %{buildroot}%{python3_sitelib}/%{pypi_name}/tests/

%files
%license LICENSE
%doc README.rst CHANGES.rst
%{python_sitelib}/*egg-info
%{python_sitelib}/%{pypi_name}
%{_bindir}/keyring
