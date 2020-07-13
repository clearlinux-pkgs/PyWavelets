#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyWavelets
Version  : 1.1.1
Release  : 27
URL      : https://files.pythonhosted.org/packages/17/6b/ef989cfb3acff2ea966c5f28a7443ccaec2ee136675dfa0366db2635f78a/PyWavelets-1.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/17/6b/ef989cfb3acff2ea966c5f28a7443ccaec2ee136675dfa0366db2635f78a/PyWavelets-1.1.1.tar.gz
Summary  : PyWavelets, wavelet transform module
Group    : Development/Tools
License  : MIT
Requires: PyWavelets-license = %{version}-%{release}
Requires: PyWavelets-python = %{version}-%{release}
Requires: PyWavelets-python3 = %{version}-%{release}
Requires: Cython
Requires: matplotlib
Requires: numpy
Requires: numpydoc
Requires: wheel
BuildRequires : Cython
BuildRequires : buildreq-distutils3
BuildRequires : matplotlib
BuildRequires : numpy
BuildRequires : numpydoc
BuildRequires : wheel

%description
* nD Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
                * 1D and 2D Forward and Inverse Stationary Wavelet Transform (Undecimated Wavelet Transform)
                * 1D and 2D Wavelet Packet decomposition and reconstruction
                * 1D Continuous Wavelet Tranfsorm
                * Computing Approximations of wavelet and scaling functions
                * Over 100 built-in wavelet filters and support for custom wavelets
                * Single and double precision calculations
                * Real and complex calculations
                * Results compatible with Matlab Wavelet Toolbox (TM)

%package license
Summary: license components for the PyWavelets package.
Group: Default

%description license
license components for the PyWavelets package.


%package python
Summary: python components for the PyWavelets package.
Group: Default
Requires: PyWavelets-python3 = %{version}-%{release}
Provides: pywavelets-python

%description python
python components for the PyWavelets package.


%package python3
Summary: python3 components for the PyWavelets package.
Group: Default
Requires: python3-core
Provides: pypi(pywavelets)
Requires: pypi(numpy)

%description python3
python3 components for the PyWavelets package.


%prep
%setup -q -n PyWavelets-1.1.1
cd %{_builddir}/PyWavelets-1.1.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583522707
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/PyWavelets
cp %{_builddir}/PyWavelets-1.1.1/LICENSE %{buildroot}/usr/share/package-licenses/PyWavelets/ee2da39132c285da4731863fcfafc9c48e1ee6c4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/PyWavelets/ee2da39132c285da4731863fcfafc9c48e1ee6c4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
