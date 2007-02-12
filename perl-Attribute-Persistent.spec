#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Attribute
%define		pnam	Persistent
Summary:	Attribute::Persistent - really lazy persistence
Summary(pl.UTF-8):   Attribute::Persistent - bardzo leniwe zachowywanie atrybutów
Name:		perl-Attribute-Persistent
Version:	1.1
Release:	1
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3d93ef5e3566c1bd54d4cb22ad76106a
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-Attribute-Handlers-Prospective
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MLDBM
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a way of abstracting away persistence of array
and hash variables.

It's useful for quick hacks when you don't care about pulling in the
right DBM library and calling tie and so on. Its job is to reduce fuss
for the lazy programmer at the cost of flexibility.

%description -l pl.UTF-8
Ten moduł udostępnia metodę na wyabstrahowanie zachowywania zmiennych
tablicowych i haszy. Jest przydatnych do szybkich hacków, kiedy nie
dba się o wyciąganie właściwej biblioteki DBM, wywoływanie jej
dowiązań itd. Zadaniem modułu jest zredukowanie zamieszania dla
leniwego programisty kosztem elastyczności.

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
%doc Change*
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
