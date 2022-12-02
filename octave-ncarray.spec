%define octpkg ncarray

Summary:	Access NetCDF files as a multi-dimensional array with Octave
Name:		octave-%{octpkg}
Version:	1.0.5
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 3.4.0
BuildRequires:	octave-netcdf >= 1.0.2
BuildRequires:	octave-statistics >= 1.0.6

Requires:	octave(api) = %{octave_api}
Requires:	octave-netcdf >= 1.0.2
Requires:	octave-statistics >= 1.0.6

Requires(post): octave
Requires(postun): octave

%description
Access a single or a collection of NetCDF files as a multi-dimensional 
array.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

# remove backup files
#find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

