%define pypi_name	keyring

Name:		python-keyring
Summary:	Python library to access the system keyring service
Version:	21.5.0
Release:	%mkrel 1
Group:		Development/Python
License:	Python
URL:		https://pypi.org/project/keyring/
Source0:	%{pypi_source}
BuildArch:	noarch

%description
The Python keyring lib provides a easy way to access the system keyring
service from python. It can be used in any application that needs safe
password storage.

This package only provides file-based pseudo-keyrings. To interface with
gnome-keyring or KWallet, please install one of python-keyring-gnome or
python-keyring-kwallet.

%package -n python3-keyring
Summary:	Python 3 library to access the system keyring service
Group:		Development/Python
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(setuptools-scm)
BuildRequires:	python3dist(toml)
Requires:	python3dist(pygobject)
%{?python_provide:%python_provide python3-keyring}

%description -n python3-keyring
The Python 3 keyring lib provides a easy way to access the system keyring
service from python 3. It can be used in any application that needs safe
password storage.

This package only provides file-based pseudo-keyrings. To interface with
gnome-keyring or KWallet, please install one of python3-keyring-gnome or
python3-keyring-kwallet.

%prep
%setup -q -n %{pypi_name}-%{version}

# drop bundled egg-info
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

# we don't ship tests they need a test environment
rm -rf %{buildroot}%{python3_sitelib}/%{pypi_name}/tests/

%files -n python3-keyring
%license LICENSE
%doc README.rst CHANGES.rst
%{python3_sitelib}/*egg-info
%{python3_sitelib}/%{pypi_name}
%{_bindir}/keyring
