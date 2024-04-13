%global octpkg ncarray

Summary:	Access NetCDF files as a multi-dimensional array with Octave
Name:		octave-ncarray
Version:	1.0.6
Release:	1
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/ncarray/
Source0:	https://downloads.sourceforge.net/project/octave/ncarray-%{version}.tar.gz

BuildRequires:  octave-devel >= 3.4.0
BuildRequires:  octave-netcdf >= 1.0.2
BuildRequires:  octave-statistics >= 1.0.6

Requires:	octave(api) = %{octave_api}
Requires:  	octave-netcdf >= 1.0.2
Requires:  	octave-statistics >= 1.0.6

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
Access a single or a collection of NetCDF files as a 
multi-dimensional array.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
# NOTE: octave crashd after the end of all tests
#octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

