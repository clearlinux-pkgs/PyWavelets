#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : PyWavelets
Version  : 0.5.2
Release  : 13
URL      : http://pypi.debian.net/PyWavelets/PyWavelets-0.5.2.tar.gz
Source0  : http://pypi.debian.net/PyWavelets/PyWavelets-0.5.2.tar.gz
Summary  : PyWavelets, wavelet transform module
Group    : Development/Tools
License  : MIT
Requires: PyWavelets-python3
Requires: PyWavelets-python
Requires: Cython
Requires: nose
Requires: numpy
Requires: numpydoc
Requires: wheel
BuildRequires : Cython
BuildRequires : numpy
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools

%description
* nD Forward and Inverse Discrete Wavelet Transform (DWT and IDWT)
                * 1D and 2D Forward and Inverse Stationary Wavelet Transform (Undecimated Wavelet Transform)
                * 1D and 2D Wavelet Packet decomposition and reconstruction
                * 1D Continuous Wavelet Tranfsorm
                * Computing Approximations of wavelet and scaling functions
                * Over 100 built-in wavelet filters and support for custom wavelets
                * Single and double precision calculations
                * Results compatibility with Matlab Wavelet Toolbox (tm)

%package python
Summary: python components for the PyWavelets package.
Group: Default
Requires: PyWavelets-python3
Provides: pywavelets-python

%description python
python components for the PyWavelets package.


%package python3
Summary: python3 components for the PyWavelets package.
Group: Default
Requires: python3-core

%description python3
python3 components for the PyWavelets package.


%prep
%setup -q -n PyWavelets-0.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1530378760
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
