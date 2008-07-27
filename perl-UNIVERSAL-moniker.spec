#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	UNIVERSAL
%define		pnam	moniker
Summary:	UNIVERSAL::moniker - guess how class would be called in real world
Summary(pl.UTF-8):	UNIVERSAL::moniker - odgadywanie nazwy obiektu w świecie rzeczywistym
Name:		perl-UNIVERSAL-moniker
Version:	0.08
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/UNIVERSAL/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e59b97ccf88f9fa68c3e5c18d7059d57
URL:		http://search.cpan.org/dist/UNIVERSAL-moniker/
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

%description -l pl.UTF-8
UNIVERSAL::moniker pozwala klasom na odgadnięcia jak w świecie
rzeczywistym nazywałby się należące do nich obiekty.

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
%{perl_vendorlib}/UNIVERSAL/*.pm
%{_mandir}/man3/*
