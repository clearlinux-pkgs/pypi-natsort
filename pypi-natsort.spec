#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-natsort
Version  : 8.1.0
Release  : 25
URL      : https://files.pythonhosted.org/packages/f7/37/207acdf07c2229a799b7a042c0977ad2372f4adb3446fba8f7703e2840e1/natsort-8.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/f7/37/207acdf07c2229a799b7a042c0977ad2372f4adb3446fba8f7703e2840e1/natsort-8.1.0.tar.gz
Summary  : Simple yet flexible natural sorting in Python.
Group    : Development/Tools
License  : MIT
Requires: pypi-natsort-bin = %{version}-%{release}
Requires: pypi-natsort-license = %{version}-%{release}
Requires: pypi-natsort-python = %{version}-%{release}
Requires: pypi-natsort-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
natsort
=======
.. image:: https://img.shields.io/pypi/v/natsort.svg
:target: https://pypi.org/project/natsort/

%package bin
Summary: bin components for the pypi-natsort package.
Group: Binaries
Requires: pypi-natsort-license = %{version}-%{release}

%description bin
bin components for the pypi-natsort package.


%package license
Summary: license components for the pypi-natsort package.
Group: Default

%description license
license components for the pypi-natsort package.


%package python
Summary: python components for the pypi-natsort package.
Group: Default
Requires: pypi-natsort-python3 = %{version}-%{release}

%description python
python components for the pypi-natsort package.


%package python3
Summary: python3 components for the pypi-natsort package.
Group: Default
Requires: python3-core
Provides: pypi(natsort)

%description python3
python3 components for the pypi-natsort package.


%prep
%setup -q -n natsort-8.1.0
cd %{_builddir}/natsort-8.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643645916
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-natsort
cp %{_builddir}/natsort-8.1.0/LICENSE %{buildroot}/usr/share/package-licenses/pypi-natsort/ec36ce814d9e7dfa1aed23f6318dca5a9e94cc21
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/natsort

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-natsort/ec36ce814d9e7dfa1aed23f6318dca5a9e94cc21

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
