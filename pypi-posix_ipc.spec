#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-posix_ipc
Version  : 1.1.1
Release  : 81
URL      : https://files.pythonhosted.org/packages/07/7f/b954f224a226960a4aa98b6c5fa3d4f3fafb20bb8461446e41b563aee863/posix_ipc-1.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/07/7f/b954f224a226960a4aa98b6c5fa3d4f3fafb20bb8461446e41b563aee863/posix_ipc-1.1.1.tar.gz
Summary  : POSIX IPC primitives (semaphores, shared memory and message queues) for Python
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: pypi-posix_ipc-license = %{version}-%{release}
Requires: pypi-posix_ipc-python = %{version}-%{release}
Requires: pypi-posix_ipc-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(posix_ipc)
BuildRequires : pypi-py
BuildRequires : pypi-pytest
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# POSIX IPC
`posix_ipc` is a Python module (written in C) that permits creation and manipulation of POSIX inter-process semaphores, shared memory and message queues on platforms supporting the POSIX Realtime Extensions a.k.a. POSIX 1003.1b-1993. This includes nearly all Unices and Windows + Cygwin ≥ 1.7.

%package license
Summary: license components for the pypi-posix_ipc package.
Group: Default

%description license
license components for the pypi-posix_ipc package.


%package python
Summary: python components for the pypi-posix_ipc package.
Group: Default
Requires: pypi-posix_ipc-python3 = %{version}-%{release}

%description python
python components for the pypi-posix_ipc package.


%package python3
Summary: python3 components for the pypi-posix_ipc package.
Group: Default
Requires: python3-core
Provides: pypi(posix_ipc)

%description python3
python3 components for the pypi-posix_ipc package.


%prep
%setup -q -n posix_ipc-1.1.1
cd %{_builddir}/posix_ipc-1.1.1
pushd ..
cp -a posix_ipc-1.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1685552172
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}}$(python -c "import sys; print(sys.path[-1])") pytest --verbose || :

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-posix_ipc
cp %{_builddir}/posix_ipc-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-posix_ipc/57efcacdcab0c0ea895d2ed8b96fb2e4ebe332ce || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-posix_ipc/57efcacdcab0c0ea895d2ed8b96fb2e4ebe332ce

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/V3/usr/lib/python3*/*
/usr/lib/python3*/*
