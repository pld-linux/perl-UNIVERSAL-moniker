#
# Conditional build:
# _with_tests		- perform "make test"
# _without_autodeps	- don't BR packages needed only for resolving deps
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	UNIVERSAL
%define	pnam	moniker
Summary:	Guess how class would be called in real world
Summary(pl):	Odgadywanie sposobu wywo³ywania klasy
Name:		perl-%{pdir}-%{pnam}
Version:	0.04
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9d995563ea5bd1f79c8e932adefd9eb7
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if 0%{!?_without_autodeps:1}%{?_with_tests:1}
BuildRequires:	perl-Lingua-EN-Inflect	>= 1.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UNIVERSAL::moniker enables classes to make a good guess at what they
would be called in the real world.

%description -l pl
UNIVERSAL::moniker w³±cza w klasach mo¿liwo¶æ odgadywania, w jaki
sposób mog± te klasy w rzeczywisto¶ci byæ wywo³ywane.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
