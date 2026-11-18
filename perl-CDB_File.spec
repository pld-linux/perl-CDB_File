#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
Summary:	CDB_File - Perl extension for access to cdb databases
Summary(pl.UTF-8):	CDB_File - rozszerzenie Perla umożliwiające dostęp do baz cdb
Name:		perl-CDB_File
Version:	1.05
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	https://www.cpan.org/authors/id/T/TO/TODDR/CDB_File-%{version}.tar.gz
# Source0-md5:	b4e3f4280abd1a2ad7509aa25712d3a0
URL:		https://metacpan.org/dist/CDB_File
BuildRequires:	perl-devel >= 1:5.8.0
%if %{with tests}
BuildRequires:	perl-B-COW
BuildRequires:	perl-Test-Fatal
BuildRequires:	perl-Test-Warnings
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CDB_File is a module which provides a Perl interface to Dan Berstein's
cdb package. cdb is a fast, reliable, lightweight package for creating
and reading constant databases.

%description -l pl.UTF-8
CDB_File jest modułem stanowiącym interfejs perlowy do pakietu cdb
Dana Bersteina. cdb jest szybkim, niezawodnym, lekkim pakietem do
odczytu i tworzenia stałych baz danych. 

%prep
%setup -q -n CDB_File-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# benchmark script, not a module
%{__rm} $RPM_BUILD_ROOT%{perl_vendorarch}/bun-x.pl

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ACKNOWLEDGE Changelog
%{perl_vendorarch}/CDB_File.pm
%dir %{perl_vendorarch}/auto/CDB_File
%attr(755,root,root) %{perl_vendorarch}/auto/CDB_File/CDB_File.so
%{_mandir}/man3/*
