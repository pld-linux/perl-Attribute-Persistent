#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Attribute
%define	pnam	Persistent
Summary:	Attribute::Persistent - Really lazy persistence
#Summary(pl):	
Name:		perl-Attribute-Persistent
Version:	1.0
Release:	1
License:	GPL/Artistic
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-26
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Attribute-Handlers-Prospective
BuildRequires:	perl-Digest-MD5
BuildRequires:	perl-MLDBM
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module provides a way of abstracting away persistence of array and
hash variables.

It's useful for quick hacks when you don't care about pulling in the
right DBM library and calling tie and so on.  Its job is to reduce fuss
for the lazy programmer at the cost of flexibility.

# %description -l pl
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Change*
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
