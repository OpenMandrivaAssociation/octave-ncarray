%define octpkg ncarray

Summary:	Access NetCDF files as a multi-dimensional array with Octave
Name:		octave-%{octpkg}
Version:	1.0.4
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.4.0

Requires:	octave(api) = %{octave_api}
Requires:	octave-netcdf >= 1.0.2
Requires:	octave-statistics >= 1.0.6

Requires(post): octave
Requires(postun): octave

%description
Access a single or a collection of NetCDF files as a multi-dimensional 
array.

This package is part of external Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

