#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-posix_ipc
Version  : 1.0.5
Release  : 64
URL      : https://files.pythonhosted.org/packages/bc/2f/9a7901aa26fb0e02a671b989ba814d059a0f45af85cea31b9c9eef7e2dda/posix_ipc-1.0.5.tar.gz
Source0  : https://files.pythonhosted.org/packages/bc/2f/9a7901aa26fb0e02a671b989ba814d059a0f45af85cea31b9c9eef7e2dda/posix_ipc-1.0.5.tar.gz
Summary  : POSIX IPC primitives (semaphores, shared memory and message queues) for Python
Group    : Development/Tools
License  : BSD-2-Clause BSD-3-Clause
Requires: pypi-posix_ipc-license = %{version}-%{release}
Requires: pypi-posix_ipc-python = %{version}-%{release}
Requires: pypi-posix_ipc-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: posix_ipc
Provides: posix_ipc-python
Provides: posix_ipc-python3
BuildRequires : py
BuildRequires : pytest

%description
manipulation of POSIX inter-process semaphores, shared memory and message 
        queues on platforms supporting the POSIX Realtime Extensions a.k.a. POSIX
        1003.1b-1993. This includes nearly all Unices and Windows + Cygwin 1.7.
        
        posix_ipc is compatible with Python 2 and 3.
        
        The latest version, contact info, sample code, etc. are available on PyPI

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
%setup -q -n posix_ipc-1.0.5
cd %{_builddir}/posix_ipc-1.0.5

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641470731
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}}$(python -c "import sys; print(sys.path[-1])") pytest --verbose || :
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-posix_ipc
cp %{_builddir}/posix_ipc-1.0.5/LICENSE %{buildroot}/usr/share/package-licenses/pypi-posix_ipc/3fc444d945dceac5bfe210716394c9c4cc4d44cd
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-posix_ipc/3fc444d945dceac5bfe210716394c9c4cc4d44cd

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
