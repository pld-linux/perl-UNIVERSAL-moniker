#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	UNIVERSAL
%define		pnam	moniker
Summary:	UNIVERSAL::moniker - guess how class would be called in real world
Summary(pl):	UNIVERSAL::moniker - odgadywanie nazwy obiektu w �wiecie rzeczywistym
Name:		perl-UNIVERSAL-moniker
Version:	0.08
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e59b97ccf88f9fa68c3e5c18d7059d57
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-Lingua-EN-Inflect	>= 1.88
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UNIVERSAL::moniker enables classes to make a good guess at what they
would be called in the real world.

%description -l pl
UNIVERSAL::moniker pozwala klasom na odgadni�cia jak w �wiecie
rzeczywistym nazywa�by si� nale��ce do nich obiekty.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

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
